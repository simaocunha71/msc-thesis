    string num=to_string(n);
    int product=0;
    for (int i=0;i<num.length();i++)
    {
        if (num[i]-'0'%2==1)
        product*=num[i]-'0';
    }
    return product;
}



