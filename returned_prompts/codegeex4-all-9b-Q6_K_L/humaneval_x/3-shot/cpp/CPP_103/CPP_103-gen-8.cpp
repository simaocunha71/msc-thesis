    if (n>m)
    return "-1";
    int i,sum=0;
    for (i=n;i<=m;i++)
    sum+=i;
    int avg=(int)round(sum/(m-n+1));
    string binary;
    while(avg>0){
        int rem=avg%2;
        binary+=to_string(rem);
        avg/=2;
    }
    reverse(binary.begin(),binary.end());
    return binary;
}