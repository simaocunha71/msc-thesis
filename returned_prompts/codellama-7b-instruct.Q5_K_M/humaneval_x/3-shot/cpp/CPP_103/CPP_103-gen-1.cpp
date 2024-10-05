    int sum=0;
    int i;
    if (n>m) return "-1";
    for (i=n;i<=m;i++){
        sum+=i;
    }
    sum=sum/(m-n+1);
    sum=round(sum);
    string result;
    while (sum>0)
    {
        if (sum%2==0) result+="0";
        else result+="1";
        sum/=2;
    }
    return result;
}



