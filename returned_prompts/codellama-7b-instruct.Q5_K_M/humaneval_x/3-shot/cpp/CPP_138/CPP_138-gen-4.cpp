    int i;
    int sum=0;
    for (i=2;i<n;i+=2)
    if (n==i+i+i+i)
    return true;
    else
    sum+=i;
    if (sum==n)
    return true;
    return false;
}



