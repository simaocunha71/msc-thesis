    int month,day,year;
    sscanf(date.c_str(),"%d-%d-%d",&month,&day,&year);
    if (month>12 || month<1)
    return false;
    if (day<1 || day>31)
    return false;
    if (month==2)
    {
        if (day>29)
        return false;
    }
    if (day==31)
    {
        if (month!=1 && month!=3 && month!=5 && month!=7 && month!=8 && month!=10 && month!=12)
        return false;
    }
    if (day==30)
    {
        if (month==2 || month==4 || month==6 || month!=9 || month!=11)
        return false;
    }
    return true;
}

