    if(n>m){
        return "-1";
    }
    int sum = 0;
    for(int i = n; i<=m; i++){
        sum += i;
    }
    sum = sum/2;
    int num = sum;
    string str = "";
    while(num !=0){
        if(num%2==0){
            str = "0" + str;
        }
        else{
            str = "1" + str;
        }
        num/=2;
    }
    if(str==""){
        str = "0";
    }
    return str;
}
int main(){
    int n,m;
    scanf("%d%d",&n,&m);
    string ans = rounded_avg(n,m);
    printf("%s\n",ans.c_str());
    return 0;
}
