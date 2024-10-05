    int sum=0;
    string digits_str=to_string(n);
    for (int i=0;i<digits_str.length();i++)
    if (digits_str[i]-'0'%2!=0)
    sum*=digits_str[i]-'0';
    return sum;
}



