    int days_in_months[12]={31,28,31,30,31,30,31,31,30,31,30,31};
    int month=stoi(date.substr(0,2));
    int day=stoi(date.substr(3,2));
    int year=stoi(date.substr(6,4));
    if (month==0 || month>12)
    return false;
    if (day==0 || day>days_in_months[month-1])
    return false;
    if (date.find("/")!=string::npos)
    return false;
    if (year%4==0 && year%100!=0 && year%400==0 && month==2 && day>28)
    return false;
    if (year%4!=0 && month==2 && day>28)
    return false;
    if (year%4==0 && year%100!=0 && month==2 && day>29)
    return false;
    return true;
}


