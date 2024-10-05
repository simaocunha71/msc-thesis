    if (x<0)
    return false;
    if (n<0)
    return false;
    if (x==1)
    return true;
    if (n==1)
    return false;
    if (int(pow(n,x))==x)
    return true;
    else
    return false;
}

