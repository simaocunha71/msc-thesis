    int res=1;
    int i;
    for (i=0;i<31;i++)
    {
        if ((n & (1<<i))!=0)
        {
            res=(res*2)%p;
        }
    }
    return res;
}



