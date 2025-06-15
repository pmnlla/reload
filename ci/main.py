from intents.intent import PresetDependency, Intent
import pkgutil, importlib
import os, sys, logging


def load_tests(HeadPkgName):
    tests = []
    pkg = importlib.import_module(HeadPkgName)
    for _, intentType, _ in pkgutil.iter_modules(pkg.__path__):
        mod = importlib.import_module(f'{HeadPkgName}.{intentType}')
        for fnc in dir(mod):
            obj = getattr(mod, fnc)
            if isinstance(obj, type) and issubclass(obj, Intent) and obj is not Intent:
                tests.append(obj)
    return tests


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.ERROR)
    logger = logging.getLogger(__name__)

    # Attempt to fetch dependencies from environment variables - otherwise apply dummy data.
    try:
        deps = PresetDependency(pr_repo = os.environ["PR_REPO"], pr_id = os.environ["PR_NUMBER"], gh_token = os.environ["GH_TOKEN"])
    except:
        deps = PresetDependency(pr_repo = "pmnlla/reload", pr_id = "1", gh_token = "asdf")

    # Configure reason log
    failures = []
        

    intent_classes = load_tests('intents')
    tests = [intent_class(deps) for intent_class in intent_classes]

    stat = True
    for test in tests:
        if not test.check():
            stat = False
            failures.append(test.FailureReason)

    for r in failures:
        logger.error(r)
        

    exit(0 if stat else 1)