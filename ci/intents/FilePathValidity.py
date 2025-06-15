
from . import intent
import logging

class FilePathValidityIntent(intent.Intent):
    def check(self):
        logger = logging.getLogger(__name__)
        self.FailureReason = "Invalid or backtracking file path"

        status = True

        for file in self.deps.files_list:
            if not file.startswith("pcb/") or ".." in file:
                logger.error(f'FAIL: {file}')
                status = False
            else:
                logger.info(f'Pass: {file}')
        
        # no files attempt to escape the pcb/ directory, assume good intent
        return status

if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")