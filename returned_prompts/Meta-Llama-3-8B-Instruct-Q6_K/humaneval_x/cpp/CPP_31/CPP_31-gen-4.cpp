    if(n < 2)
        return false;
    for(long long i = 2; i*i <= n; i++){
        if(n % i == 0)
            return false;
    }
    return true;
}

int main()
{
    long long num;
    printf("Enter a number to check if it's prime: ");
    scanf("%lld",&num);
    if(is_prime(num))
        printf("%lld is a prime number.\n",num);
    else
        printf("%lld is not a prime number.\n",num);
    return 0;
}
