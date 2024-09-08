    int x = a % 10;
    int y = b % 10;
    int product = x * y;
    return product;
}

int main()
{
    int a,b;
    printf("Enter the first number: ");
    scanf("%d", &a);
    printf("Enter the second number: ");
    scanf("%d", &b);
    printf("The product of the unit digits is: %d", multiply(a,b));
    return 0;
}

