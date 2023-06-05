import sys
import os

sys.path.append(os.path.abspath('/autoscrum/'))

from autoscrum import AutoScrum

def test_autoscrum_dummy():
    scrum = AutoScrum(os.path.abspath("tests/test-run.json"))

