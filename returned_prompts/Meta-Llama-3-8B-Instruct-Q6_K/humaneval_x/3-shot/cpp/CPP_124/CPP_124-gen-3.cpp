    int month,day,year;
    char chr;
    int i;
    for (i=0;i<date.length();i++)
    {
        chr=date[i];
        if (chr=='-')
        {
            if (i<2)
            return false;
            i++;
            continue;
        }
        if (i<2)
        {
            if (chr<'0' || chr>'9')
            return false;
            continue;
        }
        if (i<5)
        {
            if (chr<'0' || chr>'9')
            return false;
            continue;
        }
        if (i<8)
        {
            if (chr<'0' || chr>'9')
            return false;
            continue;
        }
    }
    sscanf(date.c_str(),"%d-%d-%d",&month,&day,&year);
    if (month<1 || month>12 || day<1 || day>31 || year<1000)
    return false;
    if (month==2)
    {
        if (year%4==0 && (year%100!=0 || year%400==0) && day>29)
        return false;
        else if (day>28)
        return false;
    }
    else if (month==4 || month==6 || month==9 || month==11)
    {
        if (day>30)
        return false;
    }
    else if (month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12)
    {
        if (day>31)
        return false;
    }
    return true;
}  // Return true if date is valid, otherwise false.  //


