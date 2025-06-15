from intents.intent import PresetDependency, Intent
from github import PopulateDeps
import pkgutil, importlib
import os, sys, logging
import json, requests


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

    deps = PopulateDeps.GenerateDefaultDependenciesObject()

    # Start reason log
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