    if (n == 1) return 2;
    int a = 0, b = 1, c = a + b, i = 2;
    while (i < n){
        c = a + b;
        a = b;
        b = c;
        i++;
    }
    if (is_prime(c) == 0) goto A;
    return c;
}
int is_prime(int n){
    if (n <= 1) return 0;
    for (int i = 2; i <= n / 2; i++){
        if (n % i == 0) return 0;
    }
    return 1;
}
int main() {
    int n;
    scanf("%d", &n);
    printf("%d", prime_fib(n));
    return 0;
}
