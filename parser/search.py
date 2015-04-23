#!/usr/bin/env python
import re

files = open('boards.txt', 'r')

for line in files:
  if re.match("(.*)(E|e)lections(.*)", line):
    print line