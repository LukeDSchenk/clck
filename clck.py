#/usr/bin/env python3
import argparse
import sys
import csv
import time
from timesheet import timesheet, record_time
from status import read_status, write_status

STATUS_INFO = read_status()
CURRENT_TS = STATUS_INFO[0]
STATUS = STATUS_INFO[1]
STARTTIME = STATUS_INFO[2]
STARTDATE = STATUS_INFO[3]
NOTE = STATUS_INFO[4]

def parse_args(list=sys.argv):
    welcome = """clck is a command line application that mimics a physical clock
     in system, designed for remote workers needing to track their own hours.
     The goal of this application is to make it as simple and intuitive for a general
     user (like a real clock in system!) while still providing some more in depth
     features for those who wish to use them."""

    parser = argparse.ArgumentParser(description=welcome)
    #parser.add_argument('--test', '-t', help='just an example argument')

    subparsers = parser.add_subparsers(help='sub-command help')

    in_parser = subparsers.add_parser('in', description='start the timer on the current timesheet',help='start the timer')
    in_parser.set_defaults(func=in_command)
    in_parser.add_argument('--note', '-n', help="add a brief description of what you're working on")

    out_parser = subparsers.add_parser('out',description='stop the timer on the current timesheet', help='stop the timer')
    out_parser.set_defaults(func=out_command)
    out_parser.add_argument('--discard', '-d', help='stop the timer without writing the session to a timesheet', action='store_true')

    status_parser = subparsers.add_parser('status', description='show the current status of the timer', help='show timer status')
    status_parser.set_defaults(func=status_command)

    # Calls the appropriate function and passes parsed args
    args = parser.parse_args()
    args.func(args)

# Runs on clock in command
def in_command(args):
    print("clck in!")
    if args.note:
        start_timer(note)
    else:
        start_timer()

# Runs on clock out command
def out_command(args):
    if args.discard:
        dis = input("Discard the current session without writing to a timesheet? (Y/N): ")
        while dis.lower() != 'y' and dis.lower() != 'n':
            dis = input("Discard the current session without writing to a timesheet? (Y/N): ")
        if dis.lower() == 'y':
            stop_timer(discard=True)
        else:
            stop_timer()
    else:
        stop_timer()
    print("clck out!")

def status_command(args):
    pass

def start_timer(note=''):
    global STATUS
    global STARTTIME
    global STARTDATE
    global NOTE

    if STATUS == 'ACTIVE':
        print("The timer is already active (started: {})".format(STARTDATE))
    else:
        STATUS = 'ACTIVE'
        STARTTIME = time.time()
        STARTDATE = time.ctime(STARTTIME)
        NOTE = note
        write_status(CURRENT_TS, STATUS, STARTTIME, STARTDATE, NOTE)

#Beautiful
def stop_timer(discard=False):
    global STATUS

    if STATUS == 'INACTIVE':
        print("The timer is already stopped. To start recording time, use 'clck in'.")
    else:
        STATUS = 'INACTIVE'
        write_status(CURRENT_TS, STATUS, STARTTIME, STARTDATE, NOTE)
        if discard == False:
            record_time(CURRENT_TS, STARTTIME, STARTDATE, NOTE)

def main():
    parse_args()

if __name__ == "__main__":
    main()
