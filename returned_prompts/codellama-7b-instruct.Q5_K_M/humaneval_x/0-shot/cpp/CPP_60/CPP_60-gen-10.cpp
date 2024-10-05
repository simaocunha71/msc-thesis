    if (n == 0) {
        return 0;
    }
    else {
        return n + sum_to_n(n-1);
    }
}

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("Sum from 1 to %d is: %d", n, sum_to_n(n));
}

