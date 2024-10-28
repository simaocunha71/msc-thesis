    int product=1;
    string str_n;
    str_n=to_string(n);
    int i;
    for (i=0;i<str_n.length();i++)
    {
        int d=str_n[i]-'0';
        if (d%2!=0)
        product*=d;
    }
    if (product==1) product=0;
    return product;
}



