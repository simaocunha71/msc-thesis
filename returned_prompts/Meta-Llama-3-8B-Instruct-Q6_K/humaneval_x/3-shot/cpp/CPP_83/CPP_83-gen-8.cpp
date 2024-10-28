    int count=0;
    for (int i=10^(n-1);i<10^n;i++)
    {
        if (i%10==1 || i/10^(n-1)%10==1)
        count++;
    }
    return count;
}
