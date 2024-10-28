    int sum=0;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr>=65 && chr<=90)
        sum+=chr;
    }
    return sum;
}

