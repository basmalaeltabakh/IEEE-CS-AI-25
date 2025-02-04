Day = int (input("Day : "))
Month = int (input("Month : "))
Year = int (input("Year : "))
Newday = Day + 7 
Newmonth = Month
Newyear = Year
DaysInMonth = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
                 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
if (Year%4 !=0 and Year%100 !=0) or (Year % 400 == 0):
    DaysInMonth[2]=29
if Newday > DaysInMonth[Month]:
    Newday-= DaysInMonth[Month]
    Newmonth+=1
if Month == 12 :
    Newmonth=1
    Newyear+=12
print(f"Day : {Newday}   Month : {Newmonth}  Year : {Newyear}")