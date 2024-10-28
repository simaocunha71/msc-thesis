    if(n%2==0){
        n=n/2;
        goto A;
    }
    else{
        for(int i=3;i<=n;i+=2){
            if(n%i==0){
                n=n/i;
                goto A;
            }
        }
        return n;
    }
}
int main(){
    int n;
    while(scanf("%d",&n)!=EOF){
        printf("%d",largest_prime_factor(n));
    }
    return 0;
}
