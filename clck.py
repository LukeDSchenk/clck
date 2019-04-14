import argparse
import sys
import csv
from timesheet import timesheet
from status import *

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
    in_parser.add_argument('--verbose', '-v', help='more in depth description')

    out_parser = subparsers.add_parser('out',description='stop the timer on the current timesheet', help='stop the timer')
    out_parser.set_defaults(func=out_command)
    out_parser.add_argument('--discard', '-d', help='stop the timer without writing the session to a timesheet', action='store_true')
    out_parser.add_argument('--verbose', '-v', help='more in depth description')

    # Calls the appropriate function and passes sys.argv
    args = parser.parse_args()
    args.func(args)

# Runs on clock in command
def in_command(args):
    print("clck in!")
    if args.note:
        print(args.note)

# Runs on clock out command
def out_command(args):
    if args.discard:
        print("Discard the current session without writing to a timesheet? (Y/N): ")

def start_timer():
    STARTTIME = time.time()
    STARTDATE = time.ctime(STARTTIME)

def stop_timer(STARTTIME):
    pass

def main():
    pass

if __name__ == "__main__":
    write_status(CURRENT_TS, STATUS, STARTTIME, STARTDATE, "test")
    print(read_status())
