    if(n>m)return "-1";
    int temp=m-n+1;
    int sum=0;
    for(int i=n;i<=m;i++)sum+=i;
    int ans=sum/temp;
    string ret;
    while(ans){
        ret+=char('0'+ans%2);
        ans/=2;
    }
    while(ret.length()<temp)ret="0"+ret;
    return ret;
}

int main(){
    int n,m;
    while(scanf("%d %d",&n,&m)!=EOF)printf("%s\n",rounded_avg(n,m).c_str());
    return 0;
}




```
