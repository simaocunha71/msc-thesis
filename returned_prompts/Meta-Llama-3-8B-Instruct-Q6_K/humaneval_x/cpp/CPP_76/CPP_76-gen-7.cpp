    double y = log(x) / log(n);
    return round(y) == y;

}
int main()
{
    printf("%d\n", is_simple_power(1, 4));
    printf("%d\n", is_simple_power(2, 2));
    printf("%d\n", is_simple_power(8, 2));
    printf("%d\n", is_simple_power(3, 2));
    printf("%d\n", is_simple_power(3, 1));
    printf("%d\n", is_simple_power(5, 3));
    return 0;
}

