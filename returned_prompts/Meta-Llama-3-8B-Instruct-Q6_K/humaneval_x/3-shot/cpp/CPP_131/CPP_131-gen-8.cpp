    int product=1;
    int i;
    string str=to_string(n);
    for (i=0;i<str.length();i++)
    {
        if ((str[i]-'0')%2!=0)
        product*=(str[i]-'0');
    }
    return product;
}