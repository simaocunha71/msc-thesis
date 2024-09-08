    int a = 0, b = 1, count = 1;
    while(count < n){
        int temp = a + b;
        a = b;
        b = temp;
        if(is_prime(temp)){
            count++;
        }
    }
    return b;
}

bool is_prime(int n){
    if(n <= 1) return false;
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return false;
    }
    return true;
}
int main(){
    printf("%d\n",prime_fib(10));
    return 0;
}
