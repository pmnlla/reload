from . import intent
import logging

class PresetDependency:
    def __init__ (self, author, pr_repo, pr_id, gh_token, files_list):
        self.author = author
        self.pr_repo = pr_repo
        self.pr_id = pr_id
        self.gh_token = gh_token
        self.files_list = files_list

class Intent:
    def __init__(self, deps):
        self.deps = deps
        self.FailureReason = ""
        self.Logger = logging.getLogger(__name__)

if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")