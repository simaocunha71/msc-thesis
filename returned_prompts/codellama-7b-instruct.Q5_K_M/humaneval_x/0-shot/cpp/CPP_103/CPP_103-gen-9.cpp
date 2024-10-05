    if(n>m){
        return "-1";
    }
    int sum = 0;
    for(int i = n; i<=m; i++){
        sum += i;
    }
    double avg = (double)sum/(m-n+1);
    int ans = (int)avg;
    int len = (log(ans)/log(2))+1;
    string str = "";
    for(int i = len-1;i>=0;i--){
        int tmp = ans%2;
        str += to_string(tmp);
        ans = ans/2;
    }
    return str;
}
int main(){
    int n,m;
    cin>>n>>m;
    cout<<rounded_avg(n,m);
    return 0;
}
