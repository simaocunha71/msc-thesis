    int i,j;
    for (i=2;i<100;i++)
    for (j=i+1;j<100;j++)
    if (a%i==0 && a%j==0)
    return true;
    return false;
}



