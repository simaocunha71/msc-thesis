    for  (int i=0;i<n;i++)
    for  (int j=i;j<n;j++)
    for  (int k=j;k<n;k++)
    for  (int l=k;l<n;l++)
    if  (i+j+k+l==n && i%2==0 && j%2==0 && k%2==0 && l%2==0)
    return true;

    return false;
}


