    int month,day,year;
    string month_string,day_string,year_string;
    int i;
    for (i=0;i<date.length();i++)
    {
        if (date[i]=='-')
        {
            month_string=date.substr(0,i);
            day_string=date.substr(i+1,i-i-1);
            year_string=date.substr(i+2,date.length()-1);
            break;
        }
    }
    month=stoi(month_string);
    day=stoi(day_string);
    year=stoi(year_string);
    if (date.length()==0 || (day<1 || day>31 && (month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12)) || (day<1 || day>30 && (month==4 || month==6 || month==9 || month==11)) || (day<1 || day>29 && month==2) || month<1 || month>12)
    return false;
    return true;
}


