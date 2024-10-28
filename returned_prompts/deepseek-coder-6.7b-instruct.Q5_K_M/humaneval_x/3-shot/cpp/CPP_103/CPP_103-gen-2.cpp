    if(n>m)
        return "-1";
    int avg=(n+m)/2;
    int rounded_avg=(n+m)%2==0?avg:avg+1;
    string binary="";
    while(rounded_avg>0)
    {
        binary=to_string(rounded_avg%2)+binary;
        rounded_avg/=2;
    }
    return binary;
}

