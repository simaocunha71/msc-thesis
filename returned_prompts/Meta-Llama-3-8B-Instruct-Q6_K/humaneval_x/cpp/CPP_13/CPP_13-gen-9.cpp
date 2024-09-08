    if (b == 0)
    {
        return a;
    }
    else
    {
        return greatest_common_divisor(b, a % b);
    }
}
int main()
{
    int a, b;
    printf("Enter the value of a: ");
    scanf("%d", &a);
    printf("Enter the value of b: ");
    scanf("%d", &b);
    printf("GCD of %d and %d is %d\n", a, b, greatest_common_divisor(a, b));
    return 0;
}

