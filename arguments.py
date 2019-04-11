import argparse

def init_parser():
    welcome = """clck is a command line application that mimics a physical clock
     in system, designed for remote workers needing to track their own hours.
     The goal of this application is to make it as simple and intuitive for a general
     user (like a real clock in system!) while still providing some more in depth
     features for those who wish to use them."""
    parser = argparse.ArgumentParser(description=welcome)

    parser.add_argument('--test', '-i', help='starts the timer on the current timesheet (think "Clock in")')

    args = parser.parse_args()

    test = args.test
    print(test)

if __name__ == "__main__":
    init_parser()
