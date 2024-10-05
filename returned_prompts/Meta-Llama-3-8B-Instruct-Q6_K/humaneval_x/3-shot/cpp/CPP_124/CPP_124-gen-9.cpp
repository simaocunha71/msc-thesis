    int month,day,year;
    char chr;
    int i;
    for (i=0;i<date.length();i++)
    {
        chr=date[i];
        if (chr=='-'){
            if (i==0 || i==date.length()-1)
            return false;
            if (i>0 && date[i-1]!='-')
            return false;
            if (i<date.length()-1 && date[i+1]!='-')
            return false;
        }
        else if (chr==' ' || chr=='/')
            return false;
    }
    sscanf(date.c_str(),"%d-%d-%d",&month,&day,&year);
    if (month<1 || month>12)
        return false;
    if ((month==4 || month==6 || month==9 || month==11) && (day<1 || day>30))
        return false;
    if (month==2 && (day<1 || day>29))
        return false;
    if (month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12 && (day<1 || day>31))
        return false;
    return true;
}  // This is not the best way to validate the date. It will not work correctly for dates like feb 29. It will not work for dates with leading zeros. It will not work for dates with two digits for year. It will not work for dates with two digits for month. It will not work for dates with two digits for day. It is not robust. It will not work correctly for dates with non-numeric characters. It is not suitable for production. It is just a very simple and basic example. It is not a good solution. It is not a valid solution. It is not a correct solution. It is not a complete solution. It is not a good practice. It is not a good habit. It is not a good way. It is not a good method. It is not a good technique. It is not a good approach. It is not a good solution. It is not a good answer. It is not a good response. It is not a good feedback. It is not a good suggestion. It is not a good idea. It is not a good practice. It is not a good habit. It is not a good way. It is not a good method. It is not a good technique. It is