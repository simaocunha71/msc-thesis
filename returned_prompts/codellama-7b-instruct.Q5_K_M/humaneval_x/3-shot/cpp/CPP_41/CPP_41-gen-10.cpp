    int i,j,k,m,sum=0;
    for (i=0;i<n;i++)
    for (j=i+1;j<n;j++)
    for (k=j+1;k<n;k++)
    for (m=k+1;m<n;m++)
    if ((i+j)==(k+m) || (i+k)==(j+m) || (j+k)==(i+m) || (i+m)==(j+k))
    sum+=1;
    return sum;
}

