    string num_string=to_string(n);
    int product=1;
    for (int i=0;i<num_string.length();i++)
    {
        if (num_string[i]-'0'%2==1)
        product*=num_string[i]-'0';
    }
    return product;
}

