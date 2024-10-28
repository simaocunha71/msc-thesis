    int i,j;
    for (i=2;i<10;i++)
    for (j=i+1;j<10;j++)
    if (a%i==0 && a%j==0)
    return true;

    return false;
}


