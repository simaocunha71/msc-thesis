    int i;
    for(i=2; i<=n; i+=2)
    {
        n -= i;
        if(n == 0)
            return true;
        else if(n < 0)
            return false;
    }
    return false;
}

