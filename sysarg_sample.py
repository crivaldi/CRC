#!/usr/bin/python
import sys

print("hello world")
with open(sys.argv[1], 'r') as fin:
    	print fin.read()
