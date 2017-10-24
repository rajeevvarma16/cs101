def is_leap_year(n):
    if (n%4 != 0):
        return False
    elif (n%100 != 0):
        return True
    elif (n%400 != 0):
        return False
    else:
        return True
def days_in_years(year):
    if is_leap_year(year):
        daysOfMonths = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_in_year = sum(daysOfMonths)
        return daysOfMonths,days_in_year
    else:
        daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_in_year = sum(daysOfMonths)
        return daysOfMonths,days_in_year
        
def required_days_in_year(year, month, day):
    months,no_of_days = days_in_years(year)
    if month-1 !=0:
        total_no_days_passed = sum(months[:month-1]) + day
    else:
        total_no_days_passed = day
    remaining = no_of_days - total_no_days_passed
    return remaining,total_no_days_passed

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    years = []
    days = []
    for i in range(year2 - year1):
        years.append(year1+i)
    years = years[1:]
    print years
    if len(years) != 0:
        for year in years:
            days.append(days_in_years(year)[1])   
    if (year2 - year1) == 0:
        remaining_days_in_year1,days_passed_in_year1 = required_days_in_year(year1, month1, day1)
        remaining_days_in_year2,days_passed_in_year2 = required_days_in_year(year2, month2, day2)
        return days_passed_in_year2-days_passed_in_year1
    if (year2 - year1) != 0:
        remaining_days_in_year1,days_passed_in_year1 = required_days_in_year(year1, month1, day1)
        remaining_days_in_year2,days_passed_in_year2 = required_days_in_year(year2, month2, day2)
        return remaining_days_in_year1+days_passed_in_year2+sum(days)
# Test routine
print daysBetweenDates(1900,1,1,1999,12,31)
'''
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
'''