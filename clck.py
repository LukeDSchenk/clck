import argparse
import sys

def parse_args(list=sys.argv):
    welcome = """clck is a command line application that mimics a physical clock
     in system, designed for remote workers needing to track their own hours.
     The goal of this application is to make it as simple and intuitive for a general
     user (like a real clock in system!) while still providing some more in depth
     features for those who wish to use them."""

    parser = argparse.ArgumentParser(description=welcome)
    parser.add_argument('--test', '-t', help='just an example argument')

    subparsers = parser.add_subparsers(help='sub-command help')

    in_parser = subparsers.add_parser('in', description='start the timer on the current timesheet',help='start the timer')
    in_parser.set_defaults(func=in_command)

    out_parser = subparsers.add_parser('out',description='stop the timer on the current timesheet', help='stop the timer')
    out_parser.set_defaults(func=out_command)

    args = parser.parse_args()
    args.func()

# Runs on clock in command
def in_command():
    print("clck in!")

# Runs on clock out command
def out_command():
    print("clck out!")

if __name__ == "__main__":
    parse_args()
