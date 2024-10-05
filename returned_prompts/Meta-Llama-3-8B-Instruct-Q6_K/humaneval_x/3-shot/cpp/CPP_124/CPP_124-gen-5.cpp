    int day,month,year;
    bool is_valid=true;
    char chr;
    int i;
    for (i=0;i<date.length();i++)
    {
        chr=date[i];
        if (chr=='-')
        {
            if (i<2 || i>date.length()-4)
            {
                is_valid=false;
                return is_valid;
            }
            if (i==2)
            {
                day=stoi(date.substr(0,2));
                month=stoi(date.substr(3,2));
                year=stoi(date.substr(6,4));
                if (day<1 || day>31 || month<1 || month>12 || (month==2 && day>29) || (month==4 || month==6 || month==9 || month==11 && day>30))
                {
                    is_valid=false;
                }
            }
        }
    }
    return is_valid;
}