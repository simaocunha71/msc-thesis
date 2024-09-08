    long long result = 1;
    for(int i = 1; i <= n; i++){
        result *= i;
        for(int j = 2; j <= i; j++){
            result *= j;
        }
    }
    return result;
}

int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    if(n > 0){
        printf("The Brazilian factorial of %d is %lld\n", n, special_factorial(n));
    }
    else
        printf("Please enter a positive integer.\n");
    return 0;
}

