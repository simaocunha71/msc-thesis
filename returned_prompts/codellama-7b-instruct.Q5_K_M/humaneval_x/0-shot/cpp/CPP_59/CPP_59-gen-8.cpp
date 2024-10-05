    for(int i = n; i > 0; i--){
        if(n % i == 0 && is_prime(i)){
            return i;
        }
    }
    n = n / 2;
    goto A;
}

bool is_prime(int n){

B:
    for(int i = n; i > 1; i--){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        printf("%d\n", largest_prime_factor(n));
    }
    return 0;
}
