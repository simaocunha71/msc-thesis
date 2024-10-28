    if (date.length()<10)
    return false;
    int month,day,year;
    int i;
    for (i=0;i<2;i++)
    if (date[i]<'0'||date[i]>'9')
    return false;
    month=date[0]-'0';
    day=date[1]-'0';
    year=date[3]-'0';
    year+=10*(date[2]-'0');
    year+=100*(date[4]-'0');
    year+=1000*(date[5]-'0');
    year+=10000*(date[6]-'0');
    year+=100000*(date[7]-'0');
    year+=1000000*(date[8]-'0');
    year+=10000000*(date[9]-'0');
    if ((month>=1&&month<=12)&&(day>=1&&day<=31))
    return true;
    else
    return false;
}



