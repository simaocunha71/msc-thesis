    int res = 1; 
    while (n > 0)
    {
        if (n % 2 == 1)
            res = (res * 2) % p;
        n = n / 2;
        res %= p;
    }
    return res;
}


