    if (date.empty())
    return false;
    if (date.size()!=10)
    return false;

    int month=stoi(date.substr(0,2));
    int day=stoi(date.substr(3,2));
    int year=stoi(date.substr(6,4));
    if (month<1 or month>12)
    return false;
    if (day<1 or day>31)
    return false;
    if (month==2 and day>29)
    return false;
    if (month==4 or month==6 or month==9 or month==11)
    if (day>30)
    return false;
    if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12)
    if (day>31)
    return false;

    return true;
}


