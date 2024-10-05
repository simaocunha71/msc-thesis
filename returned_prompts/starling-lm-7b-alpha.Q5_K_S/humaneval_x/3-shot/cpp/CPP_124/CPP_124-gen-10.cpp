    int i,j,k;
    int day,month,year;
    int month_days[]={31,29,31,30,31,30,31,31,30,31,30,31};
    int month_days_normal[]={31,30,31,30,31,30,31,31,30,31,30,31};
    bool valid;
    if (date.length()<5)
    {
        valid=false;
    }
    else
    {
        valid=true;
        if (date.length()!=5)
        {
            valid=false;
        }
        else
        {
            for (i=0;i<date.length();i++)
            {
                if (!((date[i]>='0')&&(date[i]<='9')))
                {
                    valid=false;
                    break;
                }
            }
        }
    }
    if (valid)
    {
        month=(date[0]-'0')*10+(date[1]-'0');
        day=(date[3]-'0')*10+(date[4]-'0');
        year=(date[6]-'0')*1000+(date[7]-'0')*100+(date[8]-'0')*10+(date[9]-'0');
        if ((month<1)||(month>12))
        {
            valid=false;
        }
        else
        {
            if (month==2)
            {
                if (year%4!=0)
                {
                    if (day<1||day>28)
                    {
                        valid=false;
                    }
                }
                else
                {
                    if (day<1||day>29)
                    {
                        valid=false;
                    }
                }
            }
            else if (month==4||month==6||month==9||month==1