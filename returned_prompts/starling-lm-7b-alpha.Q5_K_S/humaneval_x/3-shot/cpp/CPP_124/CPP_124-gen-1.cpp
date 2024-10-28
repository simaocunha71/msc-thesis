    int month,day,year;
    int i,j;
    char chr;
    bool ok=true;
    for (i=0;i<date.length();i++)
    {
        chr=date[i];
        if (chr=='-')
        {
            j=i;
        }
    }

    if (j==0||j==2)
    {
        ok=false;
    }

    if (ok)
    {
    month=atoi(&date[0]);
    day=atoi(&date[3]);
    year=atoi(&date[6]);
    if (month<1||month>12||day<1||day>31||year<0)
    {
        ok=false;
    }
    if (month==2)
    {
        if (day>29)
        {
            ok=false;
        }
    }
    if (month==4||month==6||month==9||month==11)
    {
        if (day>30)
        {
            ok=false;
        }
    }
    }
    return ok;
}


