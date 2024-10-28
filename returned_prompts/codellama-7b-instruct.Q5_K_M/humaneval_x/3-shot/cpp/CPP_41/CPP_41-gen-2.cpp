    int i;
    int j;
    int total_collisions=0;
    int collisions[n];
    for (i=0;i<n;i++)
    collisions[i]=0;
    for (i=0;i<n;i++)
    for (j=i+1;j<n;j++)
    {
        if (collisions[i]==1 || collisions[j]==1)
        continue;
        if (i==j)
        continue;
        if (i>j)
        continue;
        if (i<j && i+j==n-1)
        continue;
        collisions[i]=collisions[j]=1;
        total_collisions+=2;
    }
    return total_collisions;
}


