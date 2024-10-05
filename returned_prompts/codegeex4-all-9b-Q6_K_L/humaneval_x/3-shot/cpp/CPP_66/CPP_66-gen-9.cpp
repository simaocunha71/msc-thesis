    int sum=0;
    int i;
    for (i=0;i<s.length();i++)
    {
        char chr=s[i];
        if (chr>='A' && chr<='Z')
        sum+=int(chr);
    }
    return sum;
}

