    int i,j;
    int day,month,year;
    bool is_valid=true;
    int length;
    int tmp;

    length=date.length();
    if (length!=10 || date[2]!='-' || date[5]!='-'){
    return false;
    }
    day=0;
    tmp=0;
    for (i=3;i<length;i++){
    tmp=tmp*10+date[i]-'0';
    day=day*10+tmp%10;
    tmp/=10;
    }

    month=0;
    tmp=0;
    for (i=0;i<2;i++){
    tmp=tmp*10+date[i]-'0';
    month=month*10+tmp%10;
    tmp/=10;
    }
    if (month<1 || month>12)
    return false;

    year=0;
    tmp=0;
    for (i=3;i<4;i++){
    tmp=tmp*10+date[i]-'0';
    year=year*10+tmp%10;
    tmp/=10;
    }
    tmp=0;
    for (i=6;i<length;i++){
    tmp=tmp*10+date[i]-'0';
    year=year*10+tmp%10;
    tmp/=10;
    }

    if (year<0)
    return false;

    if (month==2 && day>29)
    return false;
    if (month==4 || month==6 || month==9 || month==11 && day>30)
    return false;
    if (month!=2 && day>31)
    return false;

    return is_valid;
}




