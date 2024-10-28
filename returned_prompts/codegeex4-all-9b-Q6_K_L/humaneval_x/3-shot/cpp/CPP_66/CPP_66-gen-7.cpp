    int sum=0;
    for (int i=0;i<s.length();i++)
    {
        char chr=s[i];
        if (chr>='A'&&chr<='Z')
        sum+=int(chr);
    }
    return sum;
}

