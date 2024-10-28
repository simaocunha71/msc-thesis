    if (a==0)
    return true;
    if (a<0)
    {
        a=-a;
    }
    int x;
    for (x=0;x<=a;x++)
    if (pow(x,3)==a)
    return true;
    return false;
}

