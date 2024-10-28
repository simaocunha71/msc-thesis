    int i;
    for (i=2;i<10;i++)
    if (a%i==0)
    {
        if (a/i<100)
        return false;
        if (is_prime(a/i))
        return true;
        else
        return false;
    }
    return false;
}

