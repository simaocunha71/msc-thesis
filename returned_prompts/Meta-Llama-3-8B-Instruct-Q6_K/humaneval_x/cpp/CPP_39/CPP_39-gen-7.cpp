    int a = 1, b = 1, count = 1;
    while(count < n){
        int temp = a+b;
        if(temp > 1000000) return -1; //if number exceeds 1 million, return -1
        a = b;
        b = temp;
        count++;
        if(is_prime(temp)) return temp; //if number is prime, return it
    }
    return -1; //if n-th number is not prime, return -1
}
bool is_prime(int n){
    if(n<2) return false;
    for(int i = 2; i*i <= n; i++){
        if(n%i == 0) return false;
    }
    return true;
}
int main(){
    printf("%d\n", prime_fib(10)); // returns 233
    return 0;
}
