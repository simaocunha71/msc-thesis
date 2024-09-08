    if(n>m){
        return "-1";
    }
    int sum=0;
    for(int i=n;i<=m;i++){
        sum+=i;
    }
    double avg=sum/(double)(m-n+1);
    int avg_int=floor(avg);
    if(avg-avg_int>0.5){
        avg_int++;
    }
    string res="";
    while(avg_int>0){
        res=(char)(avg_int%2+'0')+res;
        avg_int/=2;
    }
    return res;
}

int main()
{
    printf("%s\n",rounded_avg(1,5).c_str());
    printf("%s\n",rounded_avg(7,5).c_str());
    printf("%s\n",rounded_avg(10,20).c_str());
    printf("%s\n",rounded_avg(20,33).c_str());
    return 0;
}
