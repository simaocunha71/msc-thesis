    if (n>1)
    {
        for (int i=2;i<=n;i++)
        {
            if (n%i==0)
            {
                return y;
            }
        }
    }
    return x;
}  // not a good solution, it will not work for big numbers


