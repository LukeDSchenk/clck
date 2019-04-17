# clck
clck is a command line application that mimics a physical clock in system, designed for remote workers needing to track their own hours. The goal of this application is to make it as simple and intuitive for a general user (like a real clock in system!) while still providing some more in depth features for those who wish to use them.

## NOTICE
clck is in a VERY early stage of development. You may come across it in a state where it seemingly does nothing at all! Have no fear, when this project is ready to be truly deployed I will be sure to provide much better documentation.

## Currently supported uses
Do not modify the timesheets/timesheet.csv file. As of right now, this is the only supported timesheet, but in the near future you will be able to create multiple timesheets and change which ones you are currently recording to. 

As of right now, clck can use the following commands:
* in (--note)
* out (--discard)
* --help works for clck.py, as well as for the `in` and `out` sub-commands

All recordings are stored locally in the ./timesheets/timesheet.csv file.

## Upcoming uses and features
* Recording of timesheets to Google Sheets!!!!
* Simplified tool usage: [clck in] [clck out] will be the base use case
* Updated help menus
* `status` sub-command to show current timer status without having to read the `status.csv` file yourself
* Many more options with timesheets
* Many more options in general
* Cool stuff :)

# Thank you to everybody who enjoys this project in any way at all, this is essentially just another experience for me to learn more cool things in python, but I hope that other people will enjoy this tool once it is finished!
