    if (n>m) return "-1";
    int sum=0;
    for (int i=n;i<=m;i++) sum+=i;
    float avg=sum/(m-n+1);
    int round_avg=round(avg);
    string rounded_binary;
    for (int i=15;i>=0;i--){
        if (round_avg%2==0) rounded_binary+='0';
        if (round_avg%2==1) rounded_binary+='1';
        round_avg/=2;
    }
    return rounded_binary;
}


