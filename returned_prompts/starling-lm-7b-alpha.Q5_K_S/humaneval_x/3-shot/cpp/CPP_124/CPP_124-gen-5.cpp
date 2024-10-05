    int i,j,days;
    int month,day,year;
    int flag=0;
    char chr;
    for (i=0;i<date.length();i++)
    {
        chr=date[i];
        if (chr=='-')
        {
        flag+=1;
        }
        if (flag==0 && chr<'0' || chr>'1' || chr<'2' || chr>'9')
        {
        return false;
        }
        if (flag==1 && chr<'0' || chr>'1' || chr<'2' || chr>'9')
        {
        return false;
        }
        if (flag==2 && chr<'0' || chr>'9')
        {
        return false;
        }
    }
    int a=0;
    for (i=0;i<date.length();i++)
    {
        chr=date[i];
        if (chr=='-')
        {
        a+=1;
        }
        else
        if (a==0)
        {
        month=chr-'0';
        }
        else
        if (a==1)
        {
        day=chr-'0';
        }
        else
        {
        year=chr-'0';
        }
    }
    if (month<1 || month>12)
    return false;
    if (day<1 || day>31)
    {
    if (month!=2)
    return false;
    }
    if (day<1 || day>30)
    {
    if (month!=4 && month!=6 && month!=9 && month!=11)
    return false;
    }
    if (day<1 || day>29)
    {
    if (month!=2)
    return false;
    }
    if (year<0 || year>9999)
    return false;
    return true;
}



