    int i,j;
    int total=0;
    for (i=0;i<n;i++)
    for (j=0;j<n;j++)
    {
        if (i!=j && abs(i-j)==(n-1))
        total+=1;
    }
    return total;
}




