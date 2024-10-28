    int i=1;
    if (x==1)
    return true;
    while (x>n)
    {
        x=x/n;
        if (x==1)
        return true;
    }
    return false;
}

