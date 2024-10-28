    if (n>m)
    return "-1";
    float avg=(n+m+1)/2.0;
    int avg_int=round(avg);
    string bin_str;
    while(avg_int>0)
    {
        if(avg_int%2==1)
            bin_str='1'+bin_str;
        else
            bin_str='0'+bin_str;
        avg_int/=2;
    }
    while(bin_str.length()<4)
        bin_str='0'+bin_str;
    return bin_str;
}  