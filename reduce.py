#!/usr/bin/env python3
import sys
from collections import defaultdict

# Most popular pick-up and drop-off locations:

# Reduce Function



if(sys.argv[1]=="-1"): #popular pickup locations
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

if(sys.argv[1]=="0"): #popular dropoff location
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
elif (sys.argv[1]=="1"): #busiest hour
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

elif(sys.argv[1]=="2"): #revenue vs month
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

elif(sys.argv[1]=="3"): #revenue vs day of the week
    current_day = None
    current_revenue = 0

    for line in sys.stdin:
        day, revenue = line.strip().split('\t')
        revenue = float(revenue)
        if current_day == day:
            current_revenue += revenue
        else:
            if current_day:
                print(f"{current_day}\t{current_revenue}")
            current_revenue = revenue
            current_day = day
    if current_day == day:
        print(f"{current_day}\t{current_revenue}")

elif(sys.argv[1]=="4"): #busiest day of the week
    current_day = None
    current_count = 0

    for line in sys.stdin:
        day, count = line.strip().split('\t')
        count = int(count)
        if current_day == day:
            current_count += count
        else:
            if current_day:
                print(f"{current_day}\t{current_count}")
            current_count = count
            current_day = day
    if current_day == day:
        print(f"{current_day}\t{current_count}")

elif(sys.argv[1]=="5"): #total trips vs month
    current_month = None
    current_count = 0

    for line in sys.stdin:
        month, count = line.strip().split('\t')
        count = int(count)
        if current_month == month:
            current_count += count
        else:
            if current_month:
                print(f"{current_month}\t{current_count}")
            current_count = count
            current_month = month

    if current_month == month:
        print(f"{current_month}\t{current_count}")





    
        
