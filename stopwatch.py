# Import Library
import datetime
import time 

# Get time for start
input("Press Enter to start.")
start_time = str(datetime.datetime.now().time()).split(":")
start_hour = start_time[0]
start_minute = start_time[1]
start_second = start_time[2]

start_time = time.time()
# Get time for stop
input("Press Enter again to stop.")
stop_time = str(datetime.datetime.now().time()).split(":")
stop_hour = stop_time[0]
stop_minute = stop_time[1]
stop_second = stop_time[2]

stop_time = time.time()

elapsed_time = stop_time - start_time
hours, remainder = divmod (elapsed_time, 3600)
minutes, seconds = divmod (remainder, 60)

print(f"Elapsed time: {int(hours)} : {int(minutes)} : {int(seconds)}")