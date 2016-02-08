def answer(x,y,z):
    days = 31
    months = 12
    years = 99
    numlist = [x,y,z]
    daylist = []
    monthlist = []
    yearlist = []
    for i in sorted(numlist):
        if i <= 12 and i not in monthlist:
            monthlist.append(i)
            if len(monthlist)!=1:
                return "Ambiguous"
        else: 
            if i <= 30 and i not in daylist:
                daylist.append(i)
                if len(daylist)!=1:
                    return "Ambiguous"
            else:
                if i <= 99 and i not in yearlist:
                    yearlist.append(i)
                    if len(yearlist)!=1:
                        return "Ambiguous"
    if len(monthlist) == 0 or len(daylist) == 0 or len(yearlist) == 0:
        return "Ambiguous"

    if monthlist[0] < 10:
        month_result = "0"+str(monthlist[0])
    else: month_result = str(monthlist[0])
    if daylist[0] < 10:
        day_result = "0"+str(daylist[0]) 
    else: day_result = str(daylist[0])
    if yearlist[0] < 10:
        year_result = "0"+str(yearlist[0])
    else: year_result = str(yearlist[0])
    return "%s/%s/%s" %(month_result,day_result,year_result) 
    
print answer(12,12,13)