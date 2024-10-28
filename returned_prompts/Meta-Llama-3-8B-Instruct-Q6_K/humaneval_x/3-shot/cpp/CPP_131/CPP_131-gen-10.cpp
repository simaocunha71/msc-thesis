    int product=1;
    char chr;
    string num_str=to_string(n);
    for (int i=0;i<num_str.length();i++)
    {
        chr=num_str[i];
        if (chr-'0'%2==1)
        product*=chr-'0';
    }
    return product;
}
