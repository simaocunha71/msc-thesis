    int i;
    for (i=2;i<=n;i+=2)
    {
        int j;
        for (j=2;j<=n;j+=2)
        {
            int k;
            for (k=2;k<=n;k+=2)
            {
                int l;
                for (l=2;l<=n;l+=2)
                {
                    if (i+j+k+l==n)
                    {
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

