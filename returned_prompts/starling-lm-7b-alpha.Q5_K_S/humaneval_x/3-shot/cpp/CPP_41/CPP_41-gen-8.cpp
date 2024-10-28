    int i,j;
    int collisions=0;
    for (i=1;i<n;i++)
    for (j=i+1;j<=n;j++)
    if (i+j>n && i+j<2*n)
    collisions+=1;

    return collisions;
}


