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
    in_parser = subparsers.add_parser('in', description='start the timer on the current timesheet',
                                      help='in help')
    out_parser = subparsers.add_parser('out',description='stop the timer on the current timesheet',
                                       help='out help')

    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    parse_args()
