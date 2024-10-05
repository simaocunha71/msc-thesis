    int i,sum;
    if (n<4)
    return false;
    for (i=2;i<=n;i+=2)
    {
        sum=0;
        for (int j=0;j<4;j++)
        sum+=i;
        if (sum==n)
        return true;
    }
    return false;
}



