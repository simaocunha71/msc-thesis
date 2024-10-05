    int i,product=1;
    int chr;
    string str=to_string(n);
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        if (chr%2!=0)
        product*=chr-'0';
    }
    return product;
}



