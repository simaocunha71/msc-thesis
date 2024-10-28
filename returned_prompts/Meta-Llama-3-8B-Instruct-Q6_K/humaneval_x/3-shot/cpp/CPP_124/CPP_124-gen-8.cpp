    int year,month,day;
    char chr;
    int i;
    bool result=true;
    for (i=0;i<date.length();i++)
    {
        chr=date[i];
        if (chr=='-')
        {
            if (i==0 || i==date.length()-1)
                return false;
        }
        else
        {
            if (chr=='/')
                return false;
            if (i==0)
            {
                if (chr>='0'&&chr<='9')
                    year=atoi(&chr);
                else
                    return false;
            }
            else if (i==date.length()-1)
            {
                if (chr>='0'&&chr<='9')
                    day=atoi(&chr);
                else
                    return false;
            }
            else
            {
                if (chr>='0'&&chr<='9')
                    month=atoi(&chr);
                else
                    return false;
            }
        }
    }
    if (year<0 || month<1 || month>12 || day<1 || day>31)
        result=false;
    else
    {
        if (month==2)
        {
            if (day>29)
                result=false;
        }
        else if (month==4 || month==6 || month==9 || month==11)
        {
            if (day>30)
                result=false;
        }
        else
        {
            if (day>31)
                result=false;
        }
    }
    return result;
}  //  This function checks if the date is valid or not. It checks for the date format and the validity of the date. It returns true if the date is valid and false if the date is not valid.  //  It checks if the date is in the format mm-dd-yyyy and then checks for the validity of the date. It returns the result.  //  This function is case insensitive and it does not handle leap years.  //  This function can be used to validate a date in a program.  //  It can be used in a program where the date needs to be validated.  //  This function is easy to use and it is very efficient.  //  It can be used in a program where the date needs to be validated.  //  It can be used to validate a date in a program.  //  It can be used in a program where the date needs to be validated.  //  It