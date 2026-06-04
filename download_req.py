# subprocess : Used to execute terminal/command prompt commands from within a Python program.

# sys.executable : Returns the path of the Python interpreter currently running the script.

# subprocess.check_call() : Executes a command and waits until it finishes.

import subprocess
import sys

lib=["numpy","nltk","tensorflow"]

subprocess.check_call([
    sys.executable,
    "-m",
    "pip",
    "install",
    *lib
])


import nltk
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('wordnet')
print("done")


'''Imagine a package:

mypackage/
│
├── __main__.py
├── file1.py

You can run:

python -m mypackage

Python looks for:

mypackage/__main__.py

and executes it.'''