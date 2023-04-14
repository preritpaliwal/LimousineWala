#!/usr/bin/env python3

import sys

current_key = None
current_count = 0

# Loop over each line of input from standard input
for line in sys.stdin:
    # Parse the input key-value pair
    key, value = line.strip().split("\t")

    # If the key has changed, emit the current key and count and reset the count
    if key != current_key:
        if current_key:
            print(f"{current_key}\t{current_count}")
        current_key = key
        current_count = 0

    # Add the value to the current count
    current_count += int(value)

# Emit the final key and count
if current_key:
    print(f"{current_key}\t{current_count}")