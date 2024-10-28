    int a=0;
    int b=1;
    int c=a+b;

    for(int i=0;i<n;i++){
        a=b;
        b=c;
        c=a+b;
    }
    if(c>1000000){
        goto A;
    }
    for(int i=2;i<=sqrt(c);i++){
        if(c%i==0){
            goto A;
        }
    }
    return c;
}

int main(){
    int n;
    while(~scanf("%d",&n)){
        if(n==1){
            printf("2\n");
        }
        else{
            printf("%d\n",prime_fib(n));
        }
    }
    return 0;
}
