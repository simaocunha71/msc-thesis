int a = 1, b = 1, c = 0, i = 1;
while (i < n) {
    c = a + b;
    a = b;
    b = c;
    i++;
}
if (isprime(c)) {
    return c;
}
goto A;

int isprime(int n) {
    if (n == 2) {
        return 1;
    }
    if (n == 1 || n % 2 == 0) {
        return 0;
    }
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int n;
    while (scanf("%d", &n) == 1) {
        printf("%d\n", prime_fib(n));
    }
}
