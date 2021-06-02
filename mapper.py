#!/usr/bin/python3
import sys
import string
import re

for line in sys.stdin:
    for word in line.split():
        tags = re.findall(r'<[^>]+>', word)
        for tag in tags:
            if tag == None:
                continue
            print(tag+"\t1")
