    int i,j,k,l;
    int a,b,c,d;
    a=atoi(x.c_str());
    b=atoi(n.c_str());
    c=b/gcd(a,b);
    d=a/gcd(a,b);
    for (i=0;i<c;i++)
    for (j=0;j<d;j++)
    {
        k=a*j;
        l=b*i;
        if (k==l) return true;
    }
    return false;
}


