if (n % 2 == 0 && n != 2)
{
    return y;
}
else if (n % 2 != 0)
{
    return x;
}
else
{
    goto A;
}
}

int main()
{
    int x, y, n;
    scanf("%d %d %d", &x, &y, &n);
    printf("%d", x_or_y(n, x, y));
    return 0;
}
