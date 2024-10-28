    if(date.size() != 10)
        return false;
    if(date[2] != '-' || date[5] != '-')
        return false;
    int month = (date[0]-'0')*10 + (date[1]-'0');
    int day = (date[3]-'0')*10 + (date[4]-'0');
    int year = (date[6]-'0')*1000 + (date[7]-'0')*100 + (date[8]-'0')*10 + (date[9]-'0');
    if(month < 1 || month > 12)
        return false;
    if(day < 1 || day > 31)
        return false;
    if(month == 4 || month == 6 || month == 9 || month == 11)
    {
        if(day > 30)
            return false;
    }
    if(month == 2)
    {
        if(day > 29)
            return false;
    }
    return true;
}



