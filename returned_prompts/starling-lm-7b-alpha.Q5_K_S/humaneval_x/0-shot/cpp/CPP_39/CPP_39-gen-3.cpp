    if(n==1)
        return 2;
    if(n==2)
        return 3;
    if(n==3)
        return 5;
    if(n==4)
        return 13;
    if(n==5)
        return 89;
    int i=6;
    int fibo=0;
    while(fibo<n){
        fibo=fib(i);
        if(fibo==1)
            i+=1;
        else if(fibo%2==1)
            return fibo;
        else
            i+=2;
    }
}

int fib(int i){
    if(i==0)
        return 0;
    if(i==1)
        return 1;
    int a=0,b=1,c=0;
    while(i>0){
        c=a+b;
        a=b;
        b=c;
        i--;
    }
    return c;
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%d\n",prime_fib(n));
    return 0;
}




























































































































































































































