import os
import sys
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
python = os.path.join(dir_path, "env/Scripts/python")
script = os.path.join(dir_path, "src/watch.py")

args = ""
for arg in sys.argv:
    args = args + " " + arg

# print(python, script, args)
os.system(python + " " + script + " " + args)