    if(n==1)
        return 2;
    int a=0,b=1,c;
    for(int i=2;i<=n;i++){
        c=a+b;
        a=b;
        b=c;
        if(c==1)
            continue;
        for(int j=2;j<=sqrt(c);j++){
            if(c%j==0)
                continue A;
        }
        if(c<n)
            continue;
        if(c%n==0)
            return c;
    }
}
int main(){
    int n;
    while(scanf("%d",&n)!=EOF){
        printf("%d\n",prime_fib(n));
    }
    return 0;
}
