    string result="db";
    string tmp="";
    int i;
    for (i=0;i<8;i++)
    {
        tmp+=(decimal%2)+'0';
        decimal/=2;
    }
    result+=tmp+"db";
    return result;
}


