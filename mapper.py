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

def map(args):
    for l in sys.stdin:
        # split all lines on comma maybe
        if len(l)==0: 
            continue
        
        line = l.strip(" ").split(",")
        take = True
        # with open("mapper_log.txt","a") as f:
        #     f.write(f"{l}\n")
        #     for a in args:
        #         f.write(str(a) + " ")
        #     f.write("\nline:\t")

        #     for a in line:
        #         f.write(str(a) + "||||")
        #     f.write("\n")

        for arg in args:
            if arg[1]=='!':
                if line[arg[0]] == arg[2]:
                    take = False
                    break
            elif arg[1]=='<':
                if line[arg[0]] >= arg[2]:
                    take = False
                    break                
            elif arg[1]=='>':
                if line[arg[0]] <= arg[2]:
                    take = False
                    break
            elif arg[1]=='=':
                if line[arg[0]] != arg[2]:
                    take = False
                    break
        if take:
            key = line[0]
            val = l
            print(f"{key}\t{val}")
            with open("mapper_log.txt","a") as f:
                f.write(f"{key}\t{val}->Taken\n")
            
        


arguments = (sys.argv[1]).split('?')
for idx,a in enumerate(arguments):
    a = list(a.split(':'))
    a[0] = int(cols[a[0]])
    # with open('mapper_log.txt','a') as f:
    #     for a1 in a:
    #         f.write(str(a1) + " ")
    #     f.write("\n")
    arguments[idx] = a



map(args = arguments)