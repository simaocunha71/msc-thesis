    for(int i = 2; i <= n; i++){
        if(n % i == 0){
            if(is_prime(i)){
                return i;
            }
            else{
                continue A;
            }
        }
    }
}
int is_prime(int n){
    for(int i = 2; i < n; i++){
        if(n % i == 0){
            return 0;
        }
    }
    return 1;
}
int main(){
    int n = 13195;
    int answer = largest_prime_factor(n);
    printf("%d", answer);
    return 0;
}

