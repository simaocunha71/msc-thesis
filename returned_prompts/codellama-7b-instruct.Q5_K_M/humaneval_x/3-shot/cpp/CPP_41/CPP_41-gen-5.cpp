    int i,j,k;
    int count=0;
    for (i=0;i<n;i++)
    for (j=0;j<n;j++)
    for (k=0;k<n;k++)
    if ((i<j)&&(j<k)&&(i<k))
    count++;

    return count;
}



