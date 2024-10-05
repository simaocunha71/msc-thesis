    if (n>m) return "-1";
    float sum=0;
    for (int i=n;i<=m;i++)
    {
        sum+=i;
    }
    sum/=(m-n+1);
    int avg=(int)round(sum);
    string res=bitset<8>(avg).to_string();
    return res;
}