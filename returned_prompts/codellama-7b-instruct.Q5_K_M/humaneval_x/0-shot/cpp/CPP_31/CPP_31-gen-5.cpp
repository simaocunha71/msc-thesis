    if (n == 0 || n == 1)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;
    for (int i = 3; i * i <= n; i += 2)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}
int main()
{
    long long n;
    while (scanf("%lld", &n) != EOF)
    {
        if (is_prime(n))
            printf("true\n");
        else
            printf("false\n");
    }
    return 0;
}
