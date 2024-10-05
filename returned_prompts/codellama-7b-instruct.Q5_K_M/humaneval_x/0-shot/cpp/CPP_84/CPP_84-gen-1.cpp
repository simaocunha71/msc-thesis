    if(N==0) return "0";
    int a = N%10;
    N/=10;
    goto A;
}
int main(){
    int N;
    scanf("%d",&N);
    cout<<solve(N);
    return 0;
}
