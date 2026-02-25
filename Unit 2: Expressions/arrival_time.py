hour = int(input("Current hour (0-23): "))
minute = int(input("Current minute (0-59): "))
trip_time = int(input("Trip time in minutes: "))

current_minutes = hour*60 + minute + trip_time
arr_hour = (current_minutes//60)%24
arr_minute = current_minutes%60

print("Arrival hour is",arr_hour)
print("Arrival minutes is",arr_minute)