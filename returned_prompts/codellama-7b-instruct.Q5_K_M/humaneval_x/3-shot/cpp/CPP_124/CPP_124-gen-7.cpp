    int month,day,year;
    char separator;
    string valid_date_format="^(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])-(19|20|21)\d\d$";
    string valid_date_month="^(0[1-9]|1[0-2])";
    string valid_date_day="^(0[1-9]|[1-2][0-9]|3[0-1])";
    string valid_date_year="^(19|20|21)\d\d";
    string valid_date_range="^(0[1-9]|1[0-2])";
    if (date.length()==0)
    return false;
    if (date.length()==10)
    {
        month=date.substr(0,2);
        day=date.substr(3,2);
        year=date.substr(6,4);
        if (month.find_first_not_of(valid_date_month)==string::npos && day.find_first_not_of(valid_date_day)==string::npos && year.find_first_not_of(valid_date_year)==string::npos)
        {
            if ((month=="01" || month=="03" || month=="05" || month=="07" || month=="08" || month=="10" || month=="12") && (day>31 || day<1))
            return false;
            else if ((month=="04" || month=="06" || month=="09" || month=="11") && (day>30 || day<1))
            return false;
            else if (month=="02" && (day>29 || day<1))
            return false;
            else if (month>12 || month<1)
            return false;
            else
            return true;
        }
        else
        return false;
    }
    else
    return false;
}


