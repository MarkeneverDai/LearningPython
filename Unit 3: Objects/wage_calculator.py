start_hr = int(input("Starting hour: "))
start_min = int(input("Starting minute: "))
end_hr = int(input("Ending hour: "))
end_min = int(input("Ending minute: "))
rate = float(input("Hourly wage: "))
print()

print(f"Worked {start_hr}:{start_min:02d} to {end_hr}:{end_min:02d}")
work_mintotal = (end_hr-start_hr)*60 + (end_min-start_min)
hr_work = work_mintotal//60
part_hr_work = round((work_mintotal%60)/60,2)
total_hr = hr_work+part_hr_work
print("Total hours:",total_hr)
pay = total_hr*rate
print(f"Payment: ${pay:.2f}")