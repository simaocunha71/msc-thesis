    if (n>m)
    return "-1";

    int avg=(n+m)/2;
    string str_avg=to_string(avg);
    int i;
    int len=str_avg.length();
    int j=len-1;
    while (str_avg[j]=='9')
    {
        str_avg[j]='0';
        j-=1;
        if (j==-1)
        {
            str_avg[j]='1';
            return str_avg;
        }
    }
    str_avg[j]=(str_avg[j]+1)%2+'0';
    return str_avg;
}



