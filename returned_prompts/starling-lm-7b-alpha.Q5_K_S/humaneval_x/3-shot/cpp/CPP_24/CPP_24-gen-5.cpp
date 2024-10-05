    int i=n/2;
    while (i>0)
    {
        if (n%i==0) return i;
        i-=1;
    }
    return 1;
}


