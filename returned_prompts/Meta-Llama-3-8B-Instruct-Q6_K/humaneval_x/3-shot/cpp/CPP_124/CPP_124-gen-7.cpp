    int month, day, year;
    if (date.length()!=10) return false;
    char chr;
    int i;
    for (i=0;i<10;i++)
    {
        chr=date[i];
        if (chr=='-')
        {
            if (i<2 || i>8) return false;
        }
        else if (chr=='/') return false;
    }
    for (i=0;i<10;i++)
    {
        chr=date[i];
        if (chr=='-')
        {
            if (i<2 || i>8) return false;
        }
        else if (chr=='/') return false;
    }
    for (i=0;i<10;i++)
    {
        chr=date[i];
        if (chr=='/') return false;
    }
    for (i=0;i<4;i++)
    {
        chr=date[i];
        if (chr<'0' || chr>'9') return false;
    }
    year=atoi(&date[6]);
    for (i=4;i<6;i++)
    {
        chr=date[i];
        if (chr<'0' || chr>'9') return false;
    }
    month=atoi(&date[3]);
    for (i=0;i<2;i++)
    {
        chr=date[i];
        if (chr<'0' || chr>'9') return false;
    }
    day=atoi(&date[0]);
    if (month<1 || month>12) return false;
    if (day<1 || day>31) return false;
    if (month==2)
    {
        if (year%4==0 && year%100!=0 || year%400==0)
        {
            if (day>29) return false;
        }
        else
        {
            if (day>28) return false;
        }
    }
    else if (month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12)
    {
        if (day>31) return false;
    }
    else
    {
        if (day>30) return false;
    }
    return true;
}  // 11/24/2008 11:34:00 AM
// 11/24/2008 11:34:00 AM
// 11/24/2008 11:34:00 AM
// 11