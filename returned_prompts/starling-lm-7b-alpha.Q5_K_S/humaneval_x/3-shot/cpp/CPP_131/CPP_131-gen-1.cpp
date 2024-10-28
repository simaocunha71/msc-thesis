    int i,product=1;
    string str=to_string(n);
    for (i=0;i<str.length();i++)
    {
        if (int(str[i])%2!=0)
        product*=int(str[i]);
    }
    return product;
}

