    int i=0;
    int j;
    if (a<0)
    {
        a=-a;
    }
    if (a==0)
    {
        return true;
    }
    while (i<a)
    {
        i+=1;
        j=sqrt(i);
        if (i==j*j)
        {
            if (a==i*i)
            {
                return true;
            }
        }
    }
    return false;
}

