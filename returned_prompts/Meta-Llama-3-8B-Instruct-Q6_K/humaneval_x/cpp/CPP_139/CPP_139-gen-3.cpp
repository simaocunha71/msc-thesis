    long long result = 1;
    for(int i = 1; i <= n; i++){
        result *= i;
    }
    return result;
}

int main(){
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    printf("The Brazilian factorial of %d is: %lld\n", n, special_factorial(n));
    return 0;
}