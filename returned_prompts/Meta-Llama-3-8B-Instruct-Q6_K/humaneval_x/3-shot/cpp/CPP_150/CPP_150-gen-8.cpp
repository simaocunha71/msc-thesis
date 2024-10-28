    if(n>1)
    {
        for(int i=2;i<=n/2;i++)
        {
            if(n%i==0)
            {
                return y;
            }
        }
    }
    else
    {
        return y;
    }
    return x;
}