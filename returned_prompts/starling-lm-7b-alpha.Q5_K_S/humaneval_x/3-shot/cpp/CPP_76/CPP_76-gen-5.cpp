    int i,j,k;
    for (i=0;i<32;i++)
    for (j=0;j<32;j++)
    for (k=0;k<32;k++)
    if (n==pow(i,j)*pow(j,k))
    return true;
    return false;
}


