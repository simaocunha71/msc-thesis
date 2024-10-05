    int i,product=1;
    string s=to_string(n);
    for (i=0;i<s.length();i++)
    if (s[i]-'0'%2==1)
    product*=s[i]-'0';

    return product;
}


