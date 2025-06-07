from intents.intent import PresetDependency
from intents.FileTypes import FileTypesIntent
from intents.FilePathValidity import FilePathValidityIntent
from intents.DesignRules import DesignRulesIntent
import os, sys, logging


try:
    deps = PresetDependency(pr_repo = os.environ["PR_REPO"], pr_id = os.environ["PR_NUMBER"], gh_token = os.environ["GH_TOKEN"])
except:
    deps = PresetDependency(pr_repo = "pmnlla/reload", pr_id = "1", gh_token = "asdf")

tests = [
    FileTypesIntent(deps),
    DesignRulesIntent(deps),
    FilePathValidityIntent(deps)
]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    stat = True

    for test in tests:
        if test.check() == False:
            stat = False 
        
    if stat = False:
        exit(1)
    else:
        exit(0)
