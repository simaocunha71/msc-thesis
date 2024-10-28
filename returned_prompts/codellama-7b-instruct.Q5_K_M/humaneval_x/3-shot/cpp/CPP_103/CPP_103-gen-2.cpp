    if (n>m)
    return "-1";
    int sum=0;
    for (int i=n;i<=m;i++)
    sum+=i;
    int avg=sum/(m-n+1);
    int binary=avg;
    string binary_str="";
    while (binary)
    {
        binary_str+="1";
        binary-=1;
    }
    return binary_str;
}


