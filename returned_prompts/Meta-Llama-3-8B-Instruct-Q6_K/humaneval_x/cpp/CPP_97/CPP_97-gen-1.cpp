    int product = 0;
    int unit_digit_a = a % 10;
    int unit_digit_b = b % 10;
    product = unit_digit_a * unit_digit_b;
    return product;

}
int main()
{
    printf("%d\n",multiply(148,412));
    printf("%d\n",multiply(19,28));
    printf("%d\n",multiply(2020,1851));
    printf("%d\n",multiply(14,-15));
    return 0;
}