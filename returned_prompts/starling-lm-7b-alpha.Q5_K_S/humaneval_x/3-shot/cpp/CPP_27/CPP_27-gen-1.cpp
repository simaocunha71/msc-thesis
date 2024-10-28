    char chr;
    int i;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        if (chr>='a' && chr<='z')
        {
            str[i]=chr-32;
        }
        if (chr>='A' && chr<='Z')
        {
            str[i]=chr+32;
        }
    }
    return str;
}


