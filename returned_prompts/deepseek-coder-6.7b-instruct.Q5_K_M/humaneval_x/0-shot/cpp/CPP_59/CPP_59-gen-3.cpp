    int i = 2;
B:
    if (n % i != 0) {
        i = i + 1;
        goto B;
    }
C:
    n = n / i;
    if (n != 1) {
        goto B;
    }
    return i;
}

int main() {
    printf("%d\n", largest_prime_factor(13195));
    printf("%d\n", largest_prime_factor(2048));
    return 0;
}
*/

/*
