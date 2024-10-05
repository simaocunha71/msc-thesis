    int i;
    for (i=2;i<n;i+=2)
    if (i*(i+2)*(i+4)*(i+6)==n)
    return true;
    return false;
}