    int i;
    for (i=2;i<=n;i+=2)
    if (i+(i+2)==n)
    return true;
    if (i+(i+2)+(i+4)<=n)
    return false;
    for (i=4;i<=n;i+=2)
    if (i+(i+2)+(i+4)+(i+6)==n)
    return true;
    return false;
}


