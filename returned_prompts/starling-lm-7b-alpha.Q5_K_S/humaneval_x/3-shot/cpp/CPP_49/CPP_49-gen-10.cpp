    int i=n,j=p,result=1;
    while (i>0)
    {
        if (i%2==1)
        result=(result*j)%p;
        j=(j*j)%p;
        i/=2;
    }
    return result;
}


