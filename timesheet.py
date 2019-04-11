import csv
from datetime import datetime

class timesheet:
    def __init__(self, name=""):
        self.header = ["DATE", "START", "END", "HOURS", "NOTES"]
        self.name = self.init_name(name)

    def init_name(self, name):
        dt = datetime.now()
        if name == "":
            name = dt.strftime("%d-%m-%Y--%H:%M:%S")
        name = name + ".csv"

        return name
    
    #add a function for clock in and clock out

if __name__ == "__main__":
    ts = timesheet("")
    with open("./timesheets/" + ts.name, "w", encoding="utf-8", newline="") as new_ts:
        writer = csv.writer(new_ts)

        writer.writerow(ts.header)
