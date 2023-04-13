#!/usr/bin/env python3
import sys
from collections import defaultdict

# Most popular pick-up and drop-off locations:

# Reduce Function

curr_loc = ""
curr_count = 0

if(sys.argv[1]=="-1"):
    # total = 0
    for line in sys.stdin:
        # print(line)
    # #     continue
        key, values = line.strip().split('\t')
        # total = sum(map(int, values))
        if (key == curr_loc or curr_loc==""):
            curr_loc = key
            curr_count += int(values)
        else:
            print(curr_loc, curr_count)
            curr_count = int(values)
            curr_loc = key


    print(curr_loc, curr_count)
    
    #     # values = float(values)
    #     # Calculate the total number of trips for the location
    #     total_trips = 0
    #     for i in values:
    #         total_trips += int(i)
    #     # total_trips = sum(values)
    #     # Output result
    #     print(total_trips, key)

        
