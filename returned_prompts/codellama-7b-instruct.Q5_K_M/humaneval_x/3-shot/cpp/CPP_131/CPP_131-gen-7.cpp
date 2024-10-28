    string str=to_string(n);
    int total=0;
    for (int i=0;i<str.length();i++)
    if (str[i]-'0'%2==1)
    total*=str[i]-'0';
    return total;
}



