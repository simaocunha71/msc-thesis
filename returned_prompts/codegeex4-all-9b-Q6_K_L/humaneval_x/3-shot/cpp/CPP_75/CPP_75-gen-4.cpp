    int i,j,k;
    for (i=2;i<=a;i++)
    if (a%i==0)
    {
        for (j=2;j<i;j++)
        if (i%j==0)
        break;
        else
        {
            for (k=2;k<j;k++)
            if (j%k==0)
            break;
            else
            continue;
        }
        if (j==i)
        continue;
        else
        break;
    }
    if (i>a)
    return true;
    else
    return false;
}

