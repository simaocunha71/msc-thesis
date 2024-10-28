    if (n <= 7)
        return 0;
    if (n % 11 == 0 || n % 13 == 0)
        return 1 + fizz_buzz(n / 10);
    else
        return fizz_buzz(n / 10);
}
int main()
{
    int n = 78;
    printf("%d\n", fizz_buzz(n));
    return 0;
}

