from concurrent.futures import ThreadPoolExecutor,as_completed
from multiprocessing import Pool, cpu_count
from main import stats_page1, stats_page2, stats_page3, stats_page4, stats_page5, stats_page6, stats_page7, select_where_query  

# print(cpu_count())

processes = []
with ThreadPoolExecutor(max_workers = 4) as executor:
    processes.append ( executor.submit(stats_page1, 123) )
    processes.append ( executor.submit(stats_page2, 123) )
    processes.append ( executor.submit(stats_page3, 123) )
    processes.append ( executor.submit(stats_page4, 123) )
    processes.append ( executor.submit(stats_page5, 123) )
    processes.append ( executor.submit(stats_page6, 123) )
    processes.append ( executor.submit(stats_page7, 123) )
    # processes.append ( executor.submit(select_where_query, 123,  "pickup_datetime", where_args = "2017-01-01:2017-01-02") )

for _ in as_completed(processes):
    print("Result: ", _.result())

print(processes)