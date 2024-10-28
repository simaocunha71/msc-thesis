    int sum=0;
    for(int i=0;i<=n;i+=2)
    {
        sum+=i;
        if(sum==n)
        return true;
    }
    return false;
}

