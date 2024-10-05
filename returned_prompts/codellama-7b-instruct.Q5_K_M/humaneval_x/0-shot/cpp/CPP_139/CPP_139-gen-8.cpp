    if(n == 0) return 1;
    return n * special_factorial(n-1);
}

int main(){
    int n;
    scanf("%d", &n);
    long long result = special_factorial(n);
    printf("%lld", result);
    return 0;
}
