from pathlib import Path 
from unittest import TestSuite

def load_tests(loader,tests,pattern):
    suite = TestSuite()
    loader.testMethodPrefix = "lambda_returns"
    tests = loader.descover(
        Path(__file__).parent.as_posix(),
        pattern = "*_Test.py",
    )
    suite.addTests(tests)
    return suite