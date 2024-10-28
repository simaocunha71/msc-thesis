    int product=1;
    string str = to_string(n);
    for (int i=0;i<str.length();i++)
    {
        if (str[i]%2!=0)
        product*=str[i]-'0';
    }
    return product;
}