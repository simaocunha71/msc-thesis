    int i, count;
    count=0;
    if (n==1)
    return 2;
    else
    {
        for (i=1;i<=pow(10,n-1);i++)
        {
            if (i/10>=1 && i%10==1)
            count+=1;
            if (i%10==1)
            count+=1;
        }
        return count;
    }
}

