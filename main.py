import os

inputDir = ""
outputFolder = "/"
queryNo = 1
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
