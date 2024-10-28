    if (n>m) return "-1";
    int sum=0;
    for (int i=n;i<=m;i++)
    sum+=i;
    float avg=sum/(m-n+1);
    int avg_round=avg+0.5;
    string avg_bin=to_string(avg_round,2);
    return avg_bin;
}



