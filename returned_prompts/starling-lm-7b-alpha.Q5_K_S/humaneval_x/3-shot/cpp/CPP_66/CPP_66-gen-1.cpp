    int sum=0;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr>='A' && chr<='Z')
        {
        sum+=int(chr);
        }
    }
    return sum;
}



