#!/usr/bin/env python3
import sys
from collections import defaultdict

# Most popular pick-up and drop-off locations:

# Reduce Function



if(sys.argv[1]=="-1"):
    curr_loc = ""
    curr_count = 0  
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
elif (sys.argv[1]=="1"):
    current_hour = None
    current_count = 0
    hour = None

    for line in sys.stdin:
        # print(line)
        # continue
        line = line.strip()
        hour, count = line.split('\t', 1)
        # print(hour)
        # continue
        try:
            count = int(count)
        except ValueError:
            continue

        if current_hour == hour:
            current_count += count
        else:
            if current_hour:
                print(f"{current_hour}\t{current_count}")
            current_count = count
            current_hour = hour

    if current_hour == hour:
        print(f"{current_hour}\t{current_count}")

elif(sys.argv[1]==2): #revenue vs month
    current_month = None
    current_revenue = 0
    
    for line in sys.stdin:
        month, revenue = line.strip().split('\t')
        revenue = float(revenue)
        if current_month == month:
            current_revenue += revenue
        else:
            if current_month:
                print(f"{current_month}\t{current_revenue}")
            current_revenue = revenue
            current_month = month
    if current_month == month:
        print(f"{current_month}\t{current_revenue}")




    
        
