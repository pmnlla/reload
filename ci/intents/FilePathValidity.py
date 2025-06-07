import requests
import json
from . import intent
import logging

class FilePathValidityIntent(intent.Intent):
    def check(self):
        logger = logging.getLogger(__name__)
        data = json.loads(requests.get(f'https://api.github.com/repos/{self.deps.pr_repo}/pulls/{self.deps.pr_id}/files?per_page=1000').content)
        files = [item['filename'] for item in data]

        status = True

        for file in files:
            if not file.startswith("pcb/") or ".." in file:
                logger.error(f'FAIL: {file}')
                status = False
            else:
                logger.info(f'Pass: {file}')
        
        # no files attempt to escape the pcb/ directory, assume good intent
        return status