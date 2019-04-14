import csv

def read_status():
    with open("status.csv", "r") as infile:
        reader = csv.reader(infile)
        status = list(reader)
        status = status[1]

        return status

def write_status(current_ts, status, starttime, startdate, note):
    with open("status.csv", "w", encoding='utf-8', newline='') as infile:
        writer = csv.writer(infile)
        writer.writerow(["CURRENT", "STATUS", "START", "SDATE", "NOTE"])
        writer.writerow([current_ts, status, starttime, startdate, note])
