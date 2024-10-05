    int i,j;
    for (i=0;i<date.length();i++)
    {
        if (date[i]=='-')
        {
            if (i==0 || i==date.length()-1)
            return false;
        }
    }
    if (date[4]!='-')
    return false;

    int year,month,day;
    sscanf(date.c_str(),"%d-%d-%d",&year,&month,&day);

    if (year<0)
    return false;

    if (month<1 || month>12)
    return false;

    if (month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12)
    {
        if (day<1 || day>31)
        return false;
    }
    if (month==4 || month==6 || month==9 || month==11)
    {
        if (day<1 || day>30)
        return false;
    }
    if (month==2)
    {
        if (day<1 || day>29)
        return false;
    }
    return true;
}

