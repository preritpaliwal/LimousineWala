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
    query = input("query: (enter 0 for select where..., 1 for other)")
    if(query==1):
        data = input("myMapReduce> ")
        if data == "exit":
            print("Bye!")
            break

        sel_idx = data.find("SELECT")
        from_idx = data.find("FROM")
        where_idx = data.find("WHERE")

        sel_args = data[sel_idx+7:from_idx]
        where_args = data[where_idx+6:-1]

        mapDir = f"\'./map.py {where_args}\'"
        reduceDir = f"\'./reduce.py {sel_args}\'"
        outputDir = f"{outputFolder}/{queryNo}"
        queryNo+=1

        cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reduce {reduceDir}"
        # cmd = "ls"
        os.system(cmd)

        getOutput = f"hdfs dfs -cat {outputFolder}/*"
        os.system(cmd)
    else:
        data = input("enter 1 for most popular pickup and dropoff")
        if data == "exit":
            print("Bye!")
            break

        
        mapDir = f"\'./map.py {-1}\'"
        reduceDir = f"\'./reduce.py {-1}\'"
        outputDir = f"{outputFolder}/{queryNo}"
        queryNo+=1

        cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reduce {reduceDir}"
        # cmd = "ls"
        os.system(cmd)
