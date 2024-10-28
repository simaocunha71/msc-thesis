    int a=0,b=1;
    for(int i=0;i<n;i++){
        int c=a+b;
        a=b;
        b=c;
        if(c%2==0)
            goto A;
        if(c>1)
            for(int j=2;j<c;j++)
                if(c%j==0)
                    goto A;
        return c;
    }
}
int main(){
    int n;
    printf("Enter the number of the nth prime Fibonacci number: ");
    scanf("%d",&n);
    printf("The nth prime Fibonacci number is %d",prime_fib(n));
    return 0;
}

