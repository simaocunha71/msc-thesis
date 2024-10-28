    if (n < 10)
        return n;
    else {
        int temp = n % 10;
        if (temp % 2 == 0)
            goto A;
        else
            return n % 10 * digits(n / 10);
    }