    int product=1;
    string str=to_string(n);
    int i;
    for (i=0;i<str.length();i++)
    {
        if (str[i]%2==1)
        product*=str[i];
    }
    return product;
}

