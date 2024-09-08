    int i;
    for(i = 2; i <= n; i++){
        if(n % i == 0 && is_prime(i)){
            n = i;
            goto A;
        }
    }
    return n;
}

bool is_prime(int n){
    if(n <= 1) return false;
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return false;
    }
    return true;
}

int main(){
    int n = 13195;
    printf("Largest prime factor of %d is %d\n", n, largest_prime_factor(n));
    return 0;
}
