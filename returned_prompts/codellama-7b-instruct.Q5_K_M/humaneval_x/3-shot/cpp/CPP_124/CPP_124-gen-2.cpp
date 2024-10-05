    int month,day,year;
    int valid_months[]={31,28,31,30,31,30,31,31,30,31,30,31};
    int i;
    string month_string,day_string,year_string;
    for (i=0;i<date.length();i++)
    {
        if (date[i]=='-')
        {
            month_string=date.substr(0,i);
            day_string=date.substr(i+1,i-2);
            year_string=date.substr(i+4,i+4);
        }
    }
    month=stoi(month_string);
    day=stoi(day_string);
    year=stoi(year_string);
    if (month<1||month>12)
    return false;
    if (day<1||day>31)
    return false;
    if (valid_months[month-1]<day)
    return false;
    if (month==2&&day>29)
    return false;
    if (month==2&&day>28&&year%4!=0)
    return false;
    if (month==2&&day>28&&year%4==0)
    return true;
    return true;
}



