    if(n>m) return "-1";
    double sum=0;
    for(int i=n;i<=m;i++){
        sum+=i;
    }
    double avg=sum/(m-n+1);
    int rounded=round(avg);
    string res="";
    while(rounded>0){
        res=to_string(rounded%2)+res;
        rounded/=2;
    }
    return res;
}

