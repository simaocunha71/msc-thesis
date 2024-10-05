    int day,month,year;
    char chr;
    int i;
    for (i=0;i<date.length();i++)
    {
        chr=date[i];
        if (chr== '-')
        {
        if (i==0 || i==3)
        return false;
        }
    }
    i=0;
    while (i<date.length() && date[i]!='-')
    {
        i++;
    }
    i++;
    while (i<date.length() && date[i]!='-')
    {
        i++;
    }
    i++;
    while (i<date.length())
    {
        chr=date[i];
        if (chr>='0' && chr<='9')
        {
            day=day*10+(chr-'0');
        }
        else
        {
            if (chr=='-')
            {
            month=day;
            day=0;
            }
            else
            {
            return false;
            }
        }
        i++;
    }
    year=day;
    day=0;
    if (month<1 || month>12 || day<1 || day>31)
    return false;
    if (month==2)
    {
        if (year%4==0 && (year%100!=0 || year%400==0))
        {
            if (day>29)
            return false;
        }
        else
        {
            if (day>28)
            return false;
        }
    }
    else
    {
        if (month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12)
        {
            if (day>31)
            return false;
        }
        else
        {
            if (day>30)
            return false;
        }
    }
    return true;
}  // end of function
// This function is used to validate the given date string. It first checks the format of the date string. Then it checks the validity of the date. If the date is valid, it returns true; otherwise, it returns false. The date is considered valid if all the rules are satisfied. The rules are: the date string is not empty, the number of days is valid for the given month and year, the month is not less than 1 or higher than 12, and the date is in the format: mm-dd-yyyy.  // end of comment
// The function uses a while loop and if-else statement