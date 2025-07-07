from . import intent
import requests, json

class FilePathValidityIntent(intent.Intent):
    def check(self):
        self.FailureReason = "Pull request edits files the author does not posess the latest modification over."
        status = True
        for file in self.deps.files_list:
            # Ping github API, get last author of file.
            self.logger.info("Operating on" + file)
            data = json.loads(requests.get(f'https://api.github.com/repos/{self.deps.pr_repo}/commits?path={file}').content)
            if not len(data) == 0: # if file data does not exist, file is brand new.
                try:
                    if not data[0]["committer"]["id"] == self.deps.author:
                        status = False
                        self.logger.error("File FAILS:" + file)
                except:
                    self.logger.error(data)
                    status = False
        return status

if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")