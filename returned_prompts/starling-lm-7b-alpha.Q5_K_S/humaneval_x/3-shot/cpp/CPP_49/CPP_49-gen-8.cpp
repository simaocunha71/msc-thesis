    int res=1;
    while (n>0)
    {
        res=(res*2)%p;
        n--;
    }
    return res;
}


