    int days, months;
    int month_days[12]={31,28,31,30,31,30,31,31,30,31,30,31};
    char chr;
    int i,j;
    for (i=0;i<date.length();i++)
    {
        if (date[i]>='0' && date[i]<='9')
        {
            days=date[i]-'0';
            j=i;
            for (j=i+1;j<date.length();j++)
            {
                if (date[j]!='-')
                {
                    days=days*10+date[j]-'0';
                }
                else
                {
                    if (j==i+1)
                    {
                        months=days;
                        days=0;
                    }
                    else
                    {
                        months=days;
                        days=0;
                        i=j;
                        break;
                    }
                }
            }
            if (months>12 || days>month_days[months-1])
            {
                return false;
            }
        }
    }
    return true;
}


