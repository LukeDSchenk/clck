import csv
from datetime import datetime
import os
import time

#Multiple timesheet functionality coming soon!
class timesheet:
    def __init__(self, name=""):
        self.header = ["START", "END", "HOURS", "NOTE"]
        self.name = self.init_name(name)
        self.status = "ACTIVE"
        self.ts_folder = "./timesheets/"
        os.makedirs(self.ts_folder, exist_ok=True)
        self.create_csv()

    def init_name(self, name):
        dt = datetime.now()
        if name == "":
            name = dt.strftime("%d-%m-%Y--%H:%M:%S")

        return name

    def create_csv(self):
        with open(self.ts_folder + self.name + ".csv", "w", encoding="utf-8", newline='') as timesheet:
            writer = csv.writer(timesheet)
            writer.writerow(self.header)

def record_time(current_ts, starttime, startdate, note):
    endtime = time.time()
    end_date = time.ctime()
    hours = round(((endtime - float(starttime)) / 3600), 2)
    new_line = [startdate, end_date, hours, note]

    with open("./timesheets/" + current_ts + ".csv", "a", encoding='utf-8', newline='') as timesheet:
        writer = csv.writer(timesheet)
        writer.writerow(new_line)

if __name__ == "__main__":
    ts = timesheet("timesheet")
