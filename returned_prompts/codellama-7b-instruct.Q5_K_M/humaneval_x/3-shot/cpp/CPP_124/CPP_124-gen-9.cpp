    int month,day,year,days;
    int i;
    month=0;
    day=0;
    year=0;
    days=0;
    int flag=0;
    int flag2=0;
    for (i=0;i<date.length();i++)
    {
        if (date[i]=='-')
            flag=1;
        if (date[i]=='-')
            flag2=1;
    }
    if (flag2==2)
    {
        if (flag==2)
        {
            if (date[2]=='0'&&date[3]=='4')
            {
                year=2004;
            }
            if (date[2]=='0'&&date[3]=='0')
            {
                year=2000;
            }
            if (date[2]=='0'&&date[3]=='1')
            {
                year=2001;
            }
            if (date[2]=='0'&&date[3]=='2')
            {
                year=2002;
            }
            if (date[2]=='0'&&date[3]=='3')
            {
                year=2003;
            }
            if (date[2]=='0'&&date[3]=='5')
            {
                year=2005;
            }
            if (date[2]=='0'&&date[3]=='6')
            {
                year=2006;
            }
            if (date[2]=='0'&&date[3]=='7')
            {
                year=2007;
            }
            if (date[2]=='0'&&date[3]=='8')
            {
                year=2008;
            }
            if (date[2]=='0'&&date[3]=='9')
            {
                year=2009;
            }
            if (date[2]=='1'&&date[3]==