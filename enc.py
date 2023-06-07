import os, sys
try:
    __import__("Compile").main()
except Exception as e:
    exit(str(e))
