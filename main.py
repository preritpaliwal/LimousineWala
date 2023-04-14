import os
import time
# SELECT VendorID, tpep_pickup_datetime, RatecodeID FROM tabfj WHERE RatecodeID > 100 AND fare_amount < 10;

inputDir = "/taxi/acchaData.csv"
outputFolder = "/taxi"
queryNo = 19

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



while(True):
    data = input("\nmyMapReduce> ")
    if data == "exit":
        print("Bye!")
        break
    
    # sel_idx = data.find("SELECT")
    # from_idx = data.find("FROM")
    # where_idx = data.find("WHERE")
    
    # sel = data[sel_idx+7:from_idx]
    # where = data[where_idx+6:-1]

    # convert col name to number

    sel_args = "VendorID tpep_pickup_datetime"
    where_args = "VendorID:=:2?passenger_count:=:3.0"

    print("sel_args", sel_args)
    print("where_args",where_args)
    
    mapDir = f"\'./mapper.py {where_args}\'"
    reduceDir = f"\'./reducer.py {sel_args}\'"
    outputDir = f"{outputFolder}/umika{queryNo}"
    queryNo+=1
    
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    # cmd = "ls"
    os.system(cmd)
    time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/*"
    os.system(getOutput)