# Stop gap solution - I want to implement this with PowerShell

import os
import sys
# Retrive the directory of the project - one level up from this file
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# Get the virtualenv python
python = os.path.join(dir_path, "env/Scripts/python")
# Entry point of the script
script = os.path.join(dir_path, "src/poll.py")

# Convert args to a string, to be fed into the script
args = ""
for arg in sys.argv:
    args = args + " " + arg

# Call  up the script
os.system(python + " " + script + " " + args)