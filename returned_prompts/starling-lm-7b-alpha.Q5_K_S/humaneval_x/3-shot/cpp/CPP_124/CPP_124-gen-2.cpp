    int month,day,year;
    int i,j;
    int len;
    int flag=0;
    int temp;
    char chr;
    len=date.length();
    for (i=0;i<len;i++)
    {
        chr=date[i];
        if (chr=='-')
        flag+=1;
        else if (flag==0)
        {
        month=(int)(chr-'0');
        month*=10;
        chr=date[i+1];
        month+=(int)(chr-'0');
        }
        else if (flag==1)
        {
        day=(int)(chr-'0');
        day*=10;
        chr=date[i+1];
        day+=(int)(chr-'0');
        }
        else if (flag==2)
        {
        year=(int)(chr-'0');
        year*=10;
        chr=date[i+1];
        year+=(int)(chr-'0');
        temp=year*1000;
        year+=temp;
        temp=month;
        temp*=10;
        month+=temp;
        temp=(int)(date[i+2]-'0');
        month+=temp;
        temp=(int)(date[i+3]-'0');
        month+=temp;
        temp=day;
        temp*=10;
        day+=temp;
        temp=(int)(date[i+4]-'0');
        day+=temp;
        temp=(int)(date[i+5]-'0');
        day+=temp;
        }
    }
    if (month<1||month>12||day<1||day>31||year<0||year>9999||year<(int)('2'-(int)(date[7]-'0'))||(month==2&&day>29)||(month>2&&(month==4||month==6||month==9||month==11)&&day>30)||(month!=2&&day>31))
    return false;
   