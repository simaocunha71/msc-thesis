    int product=1;
    string str;
    char chr;
    int i;
    str=to_string(n);
    for (i=0;i<str.length();i++)
    {
        chr=str[i]-'0';
        if (chr%2!=0)
            product*=chr;
    }
    return product;
}