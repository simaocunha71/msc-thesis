    if(n<m) return "-1";
    int sum=0;
    int num=0;
    for(int i=n;i<=m;i++){
        sum+=i;
        num++;
    }
    if(num==0) return "-1";
    int avg=sum/num;
    int a=avg;
    int b=a;
    string s="";
    while(a!=0){
        s+=to_string(a%2);
        a/=2;
    }
    return s;

}
int main(){
    int n,m;
    string s;
    scanf("%d %d",&n,&m);
    s=rounded_avg(n,m);
    printf("%s\n",s.c_str());
    return 0;
}

