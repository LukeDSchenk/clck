import csv
from datetime import datetime

class timesheet:
    def __init__(self, name=""):
        self.header = ["DATE", "START", "END", "HOURS", "NOTES"]
        self.name = self.init_name(name)
        self.status = "ACTIVE"
        self.ts_folder = "./timesheets/"
        os.mkdir(self.ts_folder, exist_ok=True)

    def init_name(self, name):
        dt = datetime.now()
        if name == "":
            name = dt.strftime("%d-%m-%Y--%H:%M:%S")

        return name

    def create_csv(self):
        with open(self.ts_folder + self.name + ".csv", "w", encoding="utf-8", newline='') as timesheet:
            writer = csv.writer(timesheet)
            writer.writerow(self.header)

if __name__ == "__main__":
    ts = timesheet()
    ts2 = timesheet("create_sheet_test")
    ts.create_csv()
    ts2.create_csv()
