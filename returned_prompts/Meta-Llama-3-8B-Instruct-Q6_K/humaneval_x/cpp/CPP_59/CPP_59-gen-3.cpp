    int i;
    for(i = 2; i <= n; i++){
        if(n%i == 0){
            if(is_prime(i)){
                return i;
            }
        }
    }
    return -1;
}

int is_prime(int n){
    int i;
    if(n < 2) return 0;
    for(i = 2; i <= sqrt(n); i++){
        if(n%i == 0) return 0;
    }
    return 1;
}
int main(){
    int n;
    printf("Enter a number:");
    scanf("%d",&n);
    printf("Largest prime factor is %d\n",largest_prime_factor(n));
    return 0;
}
