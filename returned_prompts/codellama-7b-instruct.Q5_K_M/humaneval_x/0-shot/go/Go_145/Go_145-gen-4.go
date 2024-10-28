    int day, month, year, len;
    char chr;
    bool flag;
    len=date.length();
    if (len==10)
    {
        month=date[0]-'0';
        if (month<1||month>12)
        return false;
        if (month==2)
        {
        day=date[2]-'0';
        if (day<1||day>29)
        return false;
        }
        else if (month%2==0)
        {
        day=date[2]-'0';
        if (day<1||day>30)
        return false;
        }
        else
        {
        day=date[2]-'0';
        if (day<1||day>31)
        return false;
        }
        for (int i=3;i<5;i++)
        {
        chr=date[i];
        if (chr<48||chr>57)
        return false;
        }
        year=date[5]-'0';
        year+=date[6]-'0';
        year+=date[7]-'0';
        year+=date[8]-'0';
        if (year<1900||year>2020)
        return false;
        return true;
    }
    return false;
}




