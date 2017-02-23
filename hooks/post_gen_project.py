#!/usr/bin/env python3

import shutil
import os

# move the script to the parent directory and remove the project directory
shutil.move("{{ cookiecutter.script }}.py", os.path.dirname(os.getcwd()))
shutil.rmtree(os.getcwd())
