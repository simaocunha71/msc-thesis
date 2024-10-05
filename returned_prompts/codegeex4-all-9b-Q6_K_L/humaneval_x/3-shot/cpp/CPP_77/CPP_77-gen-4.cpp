    int i;
    if (a==0)
    return true;
    for (i=1;i<=abs(a);i++)
    if (i*i*i==a)
    return true;
    return false;
}

