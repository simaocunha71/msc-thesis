    int i,month,day;
    char chr;
    bool is_leap_year=false;
    int year;
    for (i=0;i<date.length();i++)
    {
        chr=date[i];
        if (chr=='-')
        {
            month=(i==1?atoi(date.substr(0,i).c_str()):atoi(date.substr(i+1,date.length()-i-2).c_str()));
            day=(i==1?atoi(date.substr(i+1,date.length()-i-2).c_str()):atoi(date.substr(0,i).c_str()));
            year=atoi(date.substr(date.length()-4,4).c_str());
            if (month<1 || month>12 || day<1 || day>31 || (month==2 && day>29)) return false;
            if (month==2 && is_leap_year)
                if (day>29) return false;
            if (month==4 || month==6 || month==9 || month==11)
                if (day>30) return false;
            if (month==1 || month==3 || month==5 || month==7 || month==8 || month==10)
                if (day>31) return false;
        }
    }
    if (year%400==0) is_leap_year=true;
    if (year%100==0) is_leap_year=false;
    if (year%4==0) is_leap_year=true;
    if (year%100!=0 && year%4==0) is_leap_year=true;
    if (month<1 || month>12) return false;
    return true;
}


































































