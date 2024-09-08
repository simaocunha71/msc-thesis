    int i;
    for(i=2; i<=n; i++){
        if(n%i==0 && is_prime(i)){
            n=n/i;
            if(n!=1)goto A;
        }
    }
    return i;
}

bool is_prime(int n){
    if(n==1 || n==0) return false;
    for(int i=2; i*i<=n; i++){
        if(n%i==0) return false;
    }
    return true;
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The largest prime factor is: %d\n", largest_prime_factor(n));
    return 0;
}

