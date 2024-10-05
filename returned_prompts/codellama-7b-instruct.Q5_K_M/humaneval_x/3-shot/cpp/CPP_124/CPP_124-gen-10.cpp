    int i=0,j=0;
    string month,day,year;
    int m,d,y;
    if (date.empty())
    return false;
    i=date.find('-');
    month=date.substr(0,i);
    day=date.substr(i+1,date.find('-',i)-i);
    year=date.substr(date.find('-',i)+1);
    m=stoi(month);
    d=stoi(day);
    y=stoi(year);
    if ((m==1||m==3||m==5||m==7||m==8||m==10||m==12)&&d>0&&d<32)
    return true;
    if ((m==4||m==6||m==9||m==11)&&d>0&&d<32)
    return true;
    if (m==2&&d>0&&d<29)
    return true;
    if (m>12||m<1)
    return false;
    if (d>31||d<1)
    return false;
    return true;
}


