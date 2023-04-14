#!/usr/bin/env python3
import sys
from collections import defaultdict

# Most popular pick-up and drop-off locations:

# Map Function

if(sys.argv[1]=="-1"):
    for line in sys.stdin:
        # print(line)
        # continue
        # Split the line into fields
        fields = line.strip().split(',')
        # Extract pick-up and drop-off locations
        pickup = fields[7]
        dropoff = fields[8]
        # Emit key-value pairs
        # yield (pickup, 1)
        # yield (dropoff, 1)
        with open("check.txt", "a") as f:
            f.write(f"{pickup} {1}")
        print(f"{pickup}\t{1}")
        print(f"{dropoff}\t{1}")
elif (sys.argv[1]=="1"):
    for line in sys.stdin:
        # print(line)
        # continue
        fields = line.strip().split(',')
        pickup_datetime = fields[1]
        pickup_hour = pickup_datetime.split(':')[0][-2:]
        print(f"{pickup_hour}\t1")
        