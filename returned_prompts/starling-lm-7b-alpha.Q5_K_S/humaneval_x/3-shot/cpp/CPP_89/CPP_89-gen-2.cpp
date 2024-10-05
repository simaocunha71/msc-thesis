    int i,j;
    int length=s.length();
    char chr;
    for (i=0;i<length;i++)
    {
        chr=s[i];
        if (chr>='a' && chr<='z')
        {
        chr+=2;
        if (chr>'z')
        chr-=26;
        }
        if (chr>='A' && chr<='Z')
        {
        chr+=2;
        if (chr>'Z')
        chr-=26;
        }
        s[i]=chr;
    }
    return s;
}


