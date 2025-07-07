import inspect
import json
import logging
import os
import requests

from intents.intent import PresetDependency

def GenerateDefaultDependenciesObject():
    logger = logging.getLogger(__name__)


    # populate environment
    try:
        pr_repo = os.environ["PR_REPO"]
        pr_id = os.environ["PR_NUMBER"]     
    except: # env vars missing, shove in dummy data - you're likely running this for the sake of seeing how a _failing_ commit behaves.
        pr_repo = "pmnlla/reload"
        pr_id = "1"
    try:
        gh_token = os.environ["GH_TOKEN"]
    except:
        gh_token = "whah"

    # start paging github api for:
    # author
    author = json.loads(requests.get(f'https://api.github.com/repos/{pr_repo}/pulls/{pr_id}').content)["user"]["id"]
    logger.info(f"Author is {author}")
    # fies
    files = [item['filename'] for item in json.loads(requests.get(f'https://api.github.com/repos/{pr_repo}/pulls/{pr_id}/files?per_page=1000').content)]
    if logging.INFO >= logging.root.level:
        for each in files:
            logger.info(f"Found file in PR: {each}")

    # assemble it all!
    deps = PresetDependency(
        author = author,
        files_list = files,
        pr_id = pr_id,
        gh_token = gh_token,
        pr_repo = pr_repo
    )
    return deps


if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")