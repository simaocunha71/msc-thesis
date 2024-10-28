    int i, max_prime = -1;

B:
    while (n % 2 == 0) {
        max_prime = 2;
        n >>= 1;
    }

C:
    for (i = 3; i <= sqrt(n); i += 2) {
        while (n % i == 0) {
            max_prime = i;
            n = n / i;
        }
    }

D:
    if (n > 2)
        max_prime = n;

E:
    return max_prime;
}

int main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    printf("%d", largest_prime_factor(number));
    return 0;
}
```


