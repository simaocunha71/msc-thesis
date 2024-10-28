    int i,j;
    for (i=0;i<n;i+=2)
    for (j=i+2;j<n;j+=2)
    if (i+j==n)
    return true;
    return false;
}


