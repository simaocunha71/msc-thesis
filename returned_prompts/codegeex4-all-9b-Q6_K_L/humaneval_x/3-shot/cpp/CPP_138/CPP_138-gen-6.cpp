    int i,j,k,m;
    for (i=2;i<n;i+=2)
    for (j=2;j<n;j+=2)
    for (k=2;k<n;k+=2)
    for (m=2;m<n;m+=2)
    if (i+j+k+m==n)
    return true;

    return false;
}

