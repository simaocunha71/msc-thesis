    int month,day,year;
    int i;
    for (i=0;i<date.length();i++)
    if (date[i]=='-')
    {
        month=atoi(date.substr(0,i).c_str());
        day=atoi(date.substr(i+1,date.length()-i-2).c_str());
        year=atoi(date.substr(i+1).c_str());
        break;
    }

    if (date[0]=='0' && date.length()>2)
    return false;

    if (date[2]=='0' && date.length()>3)
    return false;

    if (month<1 || month>12)
    return false;

    if (day<1 || day>31)
    if (month!=2 && month!=4 && month!=6 && month!=9 && month!=11)
    return false;

    if (day<1 || day>29)
    if (month==2)
    return false;

    if (year<0)
    return false;

    return true;
}


