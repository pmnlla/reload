import subprocess # check deps
from . import intent # intent deps
import logging # generic deps

class DesignRulesIntent(intent.Intent):
    def check(self):
        self.FailureReason = "PCB does not pass DRC"
        status = True

        for file in self.deps.files_list:
            if file.endswith(("kicad_pcb")):
                self.logger.info(f'Checking File for DRC Failures: {file}')
                report = subprocess.run(f"kicad-cli pcb drc --schematic-parity --severity-error --exit-code-violations -o /tmp/report ../{file}")
                if report.returncode != 0:
                    self.logger.error(f'File {file} failed!')
                    status = False
                else:
                    self.logger.info(f'File {file} passed!')
        
        # no non-kicad files are being added by repository, assume good intent
        return status

if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")