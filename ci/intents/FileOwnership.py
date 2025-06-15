from . import intent
import logging
import requests, json

class FilePathValidityIntent(intent.Intent):
    def check(self):
        logger = logging.getLogger(__name__)
        self.FailureReason = "Pull request edits files the author does not posess the latest modification over."
        status = True
        for file in self.deps.files_list:
            # Ping github API, get last author of file.
            logger.info("Operating on" + file)
            data = json.loads(requests.get(f'https://api.github.com/repos/{self.deps.pr_repo}/commits?path={file}').content)
            if not len(data) == 0: # if file data does not exist, file is brand new.
                try:
                    if not data[0]["committer"]["id"] == self.deps.author:
                        status = False
                        logger.error("File FAILS:" + file)
                except:
                    logger.error(data)
                    status = False
        return status