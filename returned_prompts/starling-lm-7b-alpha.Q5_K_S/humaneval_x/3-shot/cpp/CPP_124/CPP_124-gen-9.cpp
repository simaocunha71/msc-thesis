    int month,day,year,month_days;
    int i;
    bool is_valid=true;

    if (date.length()!=10)
    {
        is_valid=false;
        return is_valid;
    }

    month=(date[3]-'0')*10 + (date[4]-'0');
    day=(date[6]-'0')*10 + (date[7]-'0');
    year=(date[9]-'0')*1000 + (date[10]-'0')*100 + (date[11]-'0')*10 + (date[12]-'0');

    if (month<1 || month>12)
    {
        is_valid=false;
        return is_valid;
    }
    if (day<1 || day>31)
    {
        is_valid=false;
        return is_valid;
    }
    if (month==2 && day>29)
    {
        is_valid=false;
        return is_valid;
    }
    if (month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12)
    {
        if (day>31)
        {
            is_valid=false;
            return is_valid;
        }
    }
    if (month==4 || month==6 || month==9 || month==11)
    {
        if (day>30)
        {
            is_valid=false;
            return is_valid;
        }
    }
    return is_valid;
}



