    int fibs[50];
    fibs[0]=0;
    fibs[1]=1;
    int i;
    for (i=2;i<n;i++)
    {
        fibs[i]=fibs[i-1]+fibs[i-2];
    }
    return fibs[n];
}

