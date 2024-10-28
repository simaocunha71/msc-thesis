    string str=to_string(n);
    int product=0;
    for (int i=0;i<str.length();i++)
        if (str[i]-'0'%2==1)
            product*=str[i]-'0';
    return product;
}



