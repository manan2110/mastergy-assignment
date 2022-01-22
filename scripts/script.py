import datetime as dt

# a dictionary to store number of days in a month
month_days = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31,
}


def run():
    month = str(input("Enter a month : "))
    month = month.lower()
    if month in month_days.keys():
        month_index = list(month_days.keys()).index(month) + 1
    else:
        print("No such month exists. Please check the month entered")
        return None
    n = int(input("Enter number of holidays : "))
    print("Enter the holidays (after entering every date do press the enter key): ")
    holidays = []
    for i in range(n):
        temp = int(input())
        holidays.append(temp)
    working_days = []
    for i in range(1, month_days[month] + 1):
        d = dt.datetime(2022, month_index, i)
        # checking if the day is not a holiday or weekend
        if d.isoweekday() in range(1, 6) and i not in holidays:
            working_days.append(i)
    print("Number of working days are :", working_days)
