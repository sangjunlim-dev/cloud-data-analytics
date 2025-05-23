#!/usr/bin/python3

import sys

# The code is a simple MapReduce mapper that reads lines from standard input,
# splits each line into words, and outputs each word with a count of 1.
for line in sys.stdin:
    line = line.strip()
    
    words = line.split()

    for word in words:
        print(f'{word}\t{1}')

