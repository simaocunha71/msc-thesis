    if(n==1||n==0)
        return n;
    int a=fib(n-1);
    int b=fib(n-2);
    return a+b;
}

int main(){
    int n;
    while(scanf("%d",&n)!=EOF){
        printf("%d\n",fib(n));
    }
    return 0;
}
