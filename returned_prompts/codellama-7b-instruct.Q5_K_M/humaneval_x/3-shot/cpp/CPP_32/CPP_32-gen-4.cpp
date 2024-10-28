    int i;
    if (xs.size()%2!=0)
    {
        return 0;
    }
    double a=xs[0];
    double b=xs[1];
    for (i=2;i<xs.size();i+=2)
    {
        a-=b*i;
        b=xs[i+1];
    }
    return -a/b;
}



