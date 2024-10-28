    int month,day,year;
    sscanf(date.c_str(),"%d-%d-%d",&month,&day,&year);
    if (month<1||month>12||day<1||day>31||year<1)
        return false;
    if (month==2){
        if (day>29)
            return false;
        if (day==29&&year%4==0)
            return true;
        else
            return false;
    }
    if (month==4||month==6||month==9||month==11){
        if (day>30)
            return false;
    }
    return true;
}