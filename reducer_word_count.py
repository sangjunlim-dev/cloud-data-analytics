#!/usr/bin/python3
import sys
from collections import defaultdict

word_count = defaultdict(int)

# Read input from standard input
for line in sys.stdin:
    line = line.strip()
    # Split the line into word and count
    word, count = line.split('\t')
    # Convert count to integer and aggregate the counts for each word
    word_count[word] += int(count)

# Output the total count for each word
for word, count in word_count.items():
    print(f'{word}\t{count}')
