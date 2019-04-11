import csv
from datetime import datetime

def create_timesheet(name=""):
    if name != "":
        with open(name + ".csv", "w", encoding="utf-8", newline='') as new_ts:
            writer = csv.writer(new_ts)
            header = ["DATE", "START", "END", "HOURS", "NOTES"]
            
            writer.writerow(header)
            
    else:
        dt = datetime.now()
        with open("ts-" + dt.strftime("%d-%m-%Y") + ".csv", "w", encoding="utf-8", newline='') as new_ts:
            writer = csv.writer(new_ts)
            header = ["DATE", "START", "END", "HOURS", "NOTES"]
            
            writer.writerow(header)
            
if __name__ == "__main__":
    pass
