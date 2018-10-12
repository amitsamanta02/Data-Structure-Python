import datetime
import time


def timeconveter(date):
    baseYear = 2000
    print("Date:" +date)
    dateIndex = date.split("-")
    numOfYears = int(dateIndex[0])-(baseYear)
    daysOfYear = numOfYears*365
    if int(dateIndex[0]) % 4 == 00:
        leapYear = 'YES'
    else:
        leapYear = 'NO'
    numOfMonths = int(dateIndex[1]) - 1
    i=1
    daysofMonths  = 0
    while i <= numOfMonths:
    ##conditions for leapYear checking.
        if i%2 == 0:
            if i == 2:
                if leapYear == "YES":
                    daysofMonths = daysofMonths + 28
                else:
                    daysofMonths = daysofMonths + 29
            else:
                daysofMonths = daysofMonths + 30
        else:
            daysofMonths = daysofMonths + 31
        i = i+1

    totalDays = daysOfYear+daysofMonths+int(dateIndex[2])
    return  totalDays


if __name__ == "__main__":
    currTime = time.time()
    numOfDays = timeconveter('2001-12-31')
    print(numOfDays)