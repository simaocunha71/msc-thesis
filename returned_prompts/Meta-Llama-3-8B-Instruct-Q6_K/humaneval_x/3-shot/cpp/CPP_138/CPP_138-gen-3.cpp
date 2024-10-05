    for (int i=2;i<=n/2;i+=2)
    {
        if (i*(i+2)*(i+4)*(i+6)==n)
        return true;
    }
    return false;
}
