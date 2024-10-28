    string str=to_string(n);
    int sum=0;
    for (int i=0;i<str.length();i++)
    if (str[i]-'0'%2==1)
    sum*=str[i]-'0';
    return sum;
}


