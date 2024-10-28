    if (a < 10 && b < 10)
        return a * b;
    int d = 0;
    if (a >= 10 && b >= 10)
    {
        d = a % 10 * b % 10;
        a = a / 10;
        b = b / 10;
        goto A;
    }
    else if (a < 10 && b >= 10)
    {
        d = a * b % 10;
        b = b / 10;
        goto A;
    }
    else if (a >= 10 && b < 10)
    {
        d = a % 10 * b;
        a = a / 10;
        goto A;
    }
    return d;
}