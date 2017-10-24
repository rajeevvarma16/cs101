def nextDay(year, month, day):
    if day < 30:
        return year,month,day+1
    else:
        if month == 12:
            return year+1,1,1
        else:
            return year,month+1,1
    return year,month,day
print 1999,12,30 
print nextDay(1999, 12, 30)
print nextDay(2013, 1, 30)
print nextDay(2012, 1, 20)
def dateIsbefore(year1,month1,day1,year2,month2,day2):
    if year2> year1:
        return True
    if year2 == year1:
        if month2 >month1:
            return True
        if month1 == month2:
            return day2 > day1
    return False
print dateIsbefore(2012,1,1,2012,2,28)
