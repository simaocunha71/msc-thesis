    int count=0;
    int i;
    if (n==1)
    return 2;
    for (i=1;i<pow(10,n-1);i++)
    if (i%10==1||i/10==1)
    count+=1;
    return count;

}

