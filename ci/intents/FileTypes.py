import requests
import json
from . import intent
import logging

class FileTypesIntent(intent.Intent):
    def check(self):
        logger = logging.getLogger(__name__)
        self.FailureReason = "Presence of non-KiCAD files"
        data = json.loads(requests.get(f'https://api.github.com/repos/{self.deps.pr_repo}/pulls/{self.deps.pr_id}/files?per_page=1000').content)
        files = [item['filename'] for item in data]

        status = True

        for file in files:
            if not file.endswith(("kicad_dru","kicad_sch","kicad_pcb","kicad_pro", "md")):
                logger.error(f'File FAILS: {file}')
                status = False
            else:
                logger.info(f'File Passes: {file}')
        
        # no non-kicad files are being added by repository, assume good intent
        return status

        
