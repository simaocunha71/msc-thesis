    int a=0, b=1;
    int i;
    for (i=0;i<n;i++)
    {
        int c=a+b;
        a=b;
        b=c;
        if (c==2 || c==3)
        continue;
        for (int j=2;j<=sqrt(c);j++)
        {
            if (c%j==0)
            break;
            if (j==sqrt(c))
            return c;
        }
    }

}

