    int i;
    for (i=2;i<100;i++)
    if (a%i==0)
    {
        a/=i;
        i=2;
    }
    if (a>1)
    return false;
    return true;
}


