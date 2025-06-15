
from . import intent
import logging

class FileTypesIntent(intent.Intent):
    def check(self):
        logger = logging.getLogger(__name__)
        self.FailureReason = "Presence of non-KiCAD files"

        status = True

        for file in self.deps.files_list:
            if not file.endswith(("kicad_dru","kicad_sch","kicad_pcb","kicad_pro", "md")):
                logger.error(f'File FAILS: {file}')
                status = False
            else:
                logger.info(f'File Passes: {file}')
        
        # no non-kicad files are being added by repository, assume good intent
        return status

        
if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")