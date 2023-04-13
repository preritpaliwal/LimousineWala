#!/usr/bin/env python
import sys
from collections import defaultdict

# Most popular pick-up and drop-off locations:

# Reduce Function

if(sys.argv[1]==-1):
    for values, key in sys.stdin:
        # Calculate the total number of trips for the location
        total_trips = sum(values)
        # Output result
        print(total_trips, key)
        
