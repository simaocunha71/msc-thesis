    int i,product=1,digit;
    string str=to_string(n);
    for (i=0;i<str.length();i++)
    {
        digit=str[i]-'0';
        if (digit%2!=0)
        product*=digit;
    }
    return product;
}


