    int i,j;
    char chr;
    int len=s.length();
    for (i=0;i<len;i++)
    {
        chr=s[i];
        if (chr>='a' && chr<='z')
        {
        chr=chr-32;
        }
        else if (chr>='A' && chr<='Z')
        {
        chr=chr+32;
        }
        s[i]=chr;
    }
    return s;
}



