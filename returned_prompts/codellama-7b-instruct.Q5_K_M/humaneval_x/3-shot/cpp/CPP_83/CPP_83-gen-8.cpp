    int i;
    int count=0;
    for (i=10^(n-1);i<10^n;i++)
    if (i%10==1||i/10==1)
    count+=1;
    return count;
}


