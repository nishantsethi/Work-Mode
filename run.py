import time
from datetime import datetime
import csv

print("   ....    ")
print("Press ENTER to start WORK MODE")
print("and, press CTRL + C to stop the stopwatch")
print("Remeber this is only if you make sure to WORK. You are being recorderded")

# infinite loop
while True:
    try:
        input() #For ENTER
        start_time = time.time()
        now = datetime.now()
        old_t = now.strftime("%H:%M:%S")
        print("Stopwatch started...")
    except KeyboardInterrupt:
        print("Stopwatch stopped...")
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        now = datetime.now()
        date_1 = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")
        to_parse = [[total_time, old_t, current_time, date_1]]
        print("The total time:", total_time,"seconds")

        with open('work_hours.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerows(to_parse)

        break # breaking the loop