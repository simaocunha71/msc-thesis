    int months[]={31,30,31,30,31,30,31,31,30,31,30,31};
    int i,j;
    for (i=0;i<date.length();i++)
    {
        if (date[i]=='-')
        continue;
        else
        {
            if (!(i==1 || i==3 || i==5 || i==7 || i==8 || i==10 || i==12))
            {
                if (!(date[i]>='0' && date[i]<='9'))
                return false;
            }
            else
            {
                if (!(date[i]>='1' && date[i]<='9' ))
                return false;
            }
        }
    }

    if (!(date[0]>='1' && date[0]<='1'))
    return false;

    if (!(date[3]>='0' && date[3]<='9' ))
    return false;

    if (!(date[6]>='0' && date[6]<='9' ))
    return false;

    if (!(date[7]>='0' && date[7]<='9' ))
    return false;

    if (!(date[8]>='0' && date[8]<='9' ))
    return false;

    if (!(date[9]>='0' && date[9]<='9' ))
    return false;

    j=date[0]-'0';
    if (j>12 || j<1)
    return false;

    j=date[3]-'0';
    if (j>months[j-1] || j<1)
    return false;

    j=date[6]-'0';
    j+=100*(date[7]-'0');
    j+=10*(date[8]-'0');
    j+=date[9]-'0';
    if (j>2020 || j<2000)
    return false;

    return true;