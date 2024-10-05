    int i,j,k;
    int prime=1;
    for (i=2;i<=a;i++)
    for (j=2;j<i;j++)
    {
        if (i%j==0)
        {
        prime=0;
        break;
        }
    }

    if (prime==1)
    {
    for (k=2;k<a;k++)
    for (j=2;j<k;j++)
    {
        if (k%j==0)
        {
        prime=0;
        break;
        }
    }

    if (prime==1)
    {
    for (j=2;j<i;j++)
    {
        if (a%j==0)
        {
        prime=0;
        break;
        }
    }

    if (prime==1)
    return true;
    }

    }

    return false;
}

