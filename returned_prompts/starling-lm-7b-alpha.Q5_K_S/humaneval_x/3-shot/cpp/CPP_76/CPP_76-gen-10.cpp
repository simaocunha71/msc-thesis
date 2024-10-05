    int i,res=1;
    for (i=0;i<32;i++)
    {
        res*=n;
        if (res==x)
        return true;
    }
    return false;
}



