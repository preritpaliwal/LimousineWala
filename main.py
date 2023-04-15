import os
import time
# SELECT VendorID, tpep_pickup_datetime, RatecodeID FROM tabfj WHERE RatecodeID > 100 AND fare_amount < 10;

inputDir = "/taxi/temp.csv"
outputFolder = "/taxi"
queryNo = 0


cols = {'VendorID': "0",
       'tpep_pickup_datetime': "1",
       'tpep_dropoff_datetime': "2",
       'passenger_count': "3",
       'trip_distance': "4",
       'RatecodeID': "5",
       'store_and_fwd_flag': "6",
       'PULocationID': "7",
       'DOLocationID': "8",
       'payment_type': "9",
       'fare_amount': "10",
       'extra': "11",
       'mta_tax': "12",
       'tip_amount': "13",
       'tolls_amount': "14",
       'improvement_surcharge': "15",
       'total_amount': "16",
       'congestion_surcharge': "17",
       'airport_fee': "18"
       }


def select_where_query(queryNo, sel_args = None, where_args = None):
    sel_args = "VendorID tpep_pickup_datetime"
    where_args = "VendorID:=:2?passenger_count:=:3.0"

    print("sel_args", sel_args)
    print("where_args", where_args)

    mapDir = f"\'./mapper.py 0 {where_args}\'"
    reduceDir = f"\'./reducer.py 0 {sel_args}\'"
    outputDir = f"{outputFolder}/output{queryNo}"

    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/*"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)

def stats_page1(queryNo):

    print("popular pickup locations")

    mapDir = f"\'./mapper.py 1\'"
    reduceDir = f"\'./reducer.py 1\'"
    outputDir = f"{outputFolder}/output{queryNo}"
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/*"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)

def stats_page2(queryNo):
    print("popular dropoff location")

    mapDir = f"\'./mapper.py 2\'"
    reduceDir = f"\'./reducer.py 2\'"
    outputDir = f"{outputFolder}/output{queryNo}"
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/*"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)

def stats_page3(queryNo):
    print("busiest hour")
    mapDir = f"\'./mapper.py 3\'"
    reduceDir = f"\'./reducer.py 3\'"
    outputDir = f"{outputFolder}/output{queryNo}"
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/*"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)

def stats_page4(queryNo):
    print("revenue vs month")
    mapDir = f"\'./mapper.py 4\'"
    reduceDir = f"\'./reducer.py 4\'"
    outputDir = f"{outputFolder}/output{queryNo}"
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/*"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)


def stats_page5(queryNo):
    print("revenue vs day of the week")
    mapDir = f"\'./mapper.py 5\'"
    reduceDir = f"\'./reducer.py 5\'"
    outputDir = f"{outputFolder}/output{queryNo}"
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/*"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)

def stats_page6(queryNo):
    print("busiest day of the week")
    mapDir = f"\'./mapper.py 6\'"
    reduceDir = f"\'./reducer.py 6\'"
    outputDir = f"{outputFolder}/output{queryNo}"
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/*"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)

def stats_page7(queryNo):
    print("total trips vs month")
    mapDir = f"\'./mapper.py 7\'"
    reduceDir = f"\'./reducer.py 7\'"
    outputDir = f"{outputFolder}/output{queryNo}"
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/*"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)


while(True):
    data = int(input("\nmyMapReduce> "))
    if data == -1:
       print("Bye!")
       break
    queryNo = queryNo + 1
    if data == 0:
        select_where_query(queryNo)
    elif data == 1:
        stats_page1(queryNo)
    elif data == 2:
        stats_page2(queryNo)
    elif data == 3:
        stats_page3(queryNo)
    elif data == 4:
        stats_page4(queryNo)
    elif data == 5:
        stats_page5(queryNo)
    elif data == 6:
        stats_page6(queryNo)
    elif data == 7:
        stats_page7(queryNo)

   

