    if (n <= 0)
        return 0;
    else if (n == 1)
        return 0;
    else if (n == 2)
        return 2;
    else if (n == 3)
        return 0;
    else if (n == 4)
        return 2;
    else if (n == 5)
        return 4;
    else if (n == 6)
        return 8;
    else if (n == 7)
        return 14;
    else if (n == 8)
        return 28;
    else if (n == 9)
        return 58;
    else if (n == 10)
        return 118;
    else
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4);

}
int main()
{
    printf("%d\n", fib4(5));
    return 0;
}
