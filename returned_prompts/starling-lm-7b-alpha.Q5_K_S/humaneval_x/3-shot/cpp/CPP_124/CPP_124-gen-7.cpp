    int month,day;
    int i;
    for (i=0;i<date.length();i++)
    {
        if (date[i]=='-')
        {
        month=atoi(date.substr(0,i).c_str());
        day=atoi(date.substr(i+1,date.length()-i-1).c_str());
        }
    }
    if (month>12 || month<1)
    return false;
    if (day>31 && (month!=2 && month!=4 && month!=6 && month!=9 && month!=11))
    return false;
    if (day>30 && (month!=2 && month!=4 && month!=6 && month!=9 && month!=11))
    return false;
    if (day>29 && month==2)
    return false;
    if (day<1 || day==0)
    return false;
    return true;
}



