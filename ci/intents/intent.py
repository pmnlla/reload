class PresetDependency:
    def __init__ (self, pr_repo, pr_id, gh_token):
        self.pr_repo = pr_repo
        self.pr_id = pr_id
        self.gh_token = gh_token

class Intent:
    def __init__(self, deps):
        self.deps = deps
        self.FailureReason = ""
