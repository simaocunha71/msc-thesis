    int i;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr>='a'&&chr<='z')
        chr+=2;
        if (chr>='A'&&chr<='Z')
        chr+=2;
        s[i]=chr;
    }
    return s;
}


