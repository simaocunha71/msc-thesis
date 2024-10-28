    if(n>m)
    return "-1";
    int avg=(n+m)/2;
    avg=round(avg);
    string binary="";
    while(avg>0)
    {
        binary=to_string(avg%2)+binary;
        avg=avg/2;
    }
    return binary;
}


