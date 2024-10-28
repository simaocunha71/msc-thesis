    int i,j,k;
    for (i=1;i<100;i++)
    for (j=i+1;j<100;j++)
    for (k=j+1;k<100;k++)
    if ((i*j*k)==a)
    return true;

    return false;
}


