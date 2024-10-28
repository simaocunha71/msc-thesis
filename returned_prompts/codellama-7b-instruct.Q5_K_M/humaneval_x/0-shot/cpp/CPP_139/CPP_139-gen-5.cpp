    if (n == 1)
        return 1;
    else{
        long long result = special_factorial(n-1);
        result *= n;
        return result;
    }
}
int main(){
    long long n;
    scanf("%lld", &n);
    printf("%lld", special_factorial(n));
    return 0;
}
