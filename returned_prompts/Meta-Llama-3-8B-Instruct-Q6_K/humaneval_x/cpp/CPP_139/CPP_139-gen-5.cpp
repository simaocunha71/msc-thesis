    long long fact = 1;

    for(int i = 1; i <= n; i++){
        fact *= i;
    }
    return fact;
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The special factorial of %d is %lld\n", n, special_factorial(n));
    return 0;
}
