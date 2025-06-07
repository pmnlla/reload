import requests
import json
import subprocess # check deps
from . import intent # intent deps
import logging # generic deps

class DesignRulesIntent(intent.Intent):
    def check(self):
        logger = logging.getLogger(__name__)
        data = json.loads(requests.get(f'https://api.github.com/repos/{self.deps.pr_repo}/pulls/{self.deps.pr_id}/files?per_page=1000').content)
        files = [item['filename'] for item in data]

        status = True

        for file in files:
            if file.endswith(("kicad_pcb")):
                logger.info(f'Checking File for DRC Failures: {file}')
                report = subprocess.run(f"kicad-cli pcb drc --schematic-parity --severity-error --exit-code-violations -o /tmp/report ../{file}")
                if report.returncode != 0:
                    logger.error(f'File {file} failed!')
                    status = False
                else:
                    logger.info(f'File {file} passed!')
        
        # no non-kicad files are being added by repository, assume good intent
        return status

