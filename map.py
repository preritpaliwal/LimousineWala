#!/usr/bin/env python
import sys
from collections import defaultdict

# Most popular pick-up and drop-off locations:

# Map Function

if(sys.argv[1]==-1):
    for line in sys.stdin:
        # Split the line into fields
        fields = line.strip().split(',')
        # Extract pick-up and drop-off locations
        pickup = fields[5]
        dropoff = fields[6]
        # Emit key-value pairs
        # yield (pickup, 1)
        # yield (dropoff, 1)
        print(pickup, 1)
        print(dropoff, 1)
    