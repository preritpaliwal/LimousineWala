#!/usr/bin/env python3
import sys

cols = {'VendorID':"0",
        'tpep_pickup_datetime':"1", 
        'tpep_dropoff_datetime':"2",
        'passenger_count':"3", 
        'trip_distance':"4", 
        'RatecodeID':"5", 
        'store_and_fwd_flag':"6",       
        'PULocationID':"7", 
        'DOLocationID':"8", 
        'payment_type':"9", 
        'fare_amount':"10", 
        'extra':"11",       
        'mta_tax':"12", 
        'tip_amount':"13", 
        'tolls_amount':"14", 
        'improvement_surcharge':"15",       
        'total_amount':"16", 
        'congestion_surcharge':"17",
        'airport_fee':"18"

        }

def tokenise(sel):
    global cols
    # print(sel)
    curArg = ""
    sel_args = []
    for s in sel:
        # print("curArg: ",curArg)
        if(s==','):
            sel_args += [int(cols[curArg])]
            curArg = ""
        elif s==' ':
            continue
        else:
            curArg += s
    if curArg!="":
        sel_args += [int(cols[curArg])]
    return sel_args


arguments = []
for arg in sys.argv[1:]:
    arguments.append(int(cols[arg]))

def reduce(args):
    for line in sys.stdin:
        # split all lines on comma maybe
        if line[0] == '\t':
            continue
        # print(line)
        # continue
        with open("reducer_log.txt","a") as f:
            for a in args:
                f.write(str(a) + " ")
            f.write("\n")
            f.write(str(line) + "\n")
        # continue
        key,val = line.strip(" ").split("\t")
        val = val.split(',')
        for i in args:
            print(val[i],end=",")
        print("")
        pass

reduce(args = arguments)
