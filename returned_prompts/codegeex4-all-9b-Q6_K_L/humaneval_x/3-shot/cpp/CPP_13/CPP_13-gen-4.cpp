    int c;
    c=b;
    while (c!=0)
    {
    c=a%b;
    a=b;
    b=c;
    }
    return a;
}

