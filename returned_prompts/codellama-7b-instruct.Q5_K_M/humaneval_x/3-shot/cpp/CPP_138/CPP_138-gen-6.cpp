    if (n%2!=0)
    return false;
    else
    {
        int i;
        int sum=0;
        for (i=2;i<=n;i+=2)
        sum+=i;
        if (sum==n)
        return true;
        else
        return false;
    }
}


