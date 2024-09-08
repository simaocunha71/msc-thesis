    int a=0,b=1,c;
    int count=0;
    while(count<n){
        c=a+b;
        a=b;
        b=c;
        if(is_prime(c)){
            count++;
        }
    }
    return c;
}
bool is_prime(int x){
    if(x<2) return false;
    for(int i=2; i*i<=x; i++)
        if(x%i==0)
            return false;
    return true;
}

int main(){
    int n;
    printf("Enter the value of n:");
    scanf("%d",&n);
    printf("%d",prime_fib(n));
    return 0;
}
