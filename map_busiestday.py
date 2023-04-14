#!/usr/bin/env python3

import sys
import csv

# Define the function to process each input record
def process_input(record):
    # Parse the input record using the CSV module
    try:
        row = next(csv.reader([record]))
    except:
        return None

    # Extract the pickup datetime field
    try:
        pickup_datetime = row[1]
        day_of_week = pickup_datetime.split()[0]
    except:
        return None

    # Emit the pickup hour and day of week as the key and a count of 1 as the value
    return (day_of_week, 1)

# Loop over each line of input from standard input
for line in sys.stdin:
    # Process the input record and emit key-value pairs
    result = process_input(line.strip())
    if result:
        key, value = result
        print(f"{key}\t{value}")
