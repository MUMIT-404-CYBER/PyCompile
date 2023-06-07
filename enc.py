import os, sys
try:
    __import__("Compile").Main()
except Exception as e:
    exit(str(e))
