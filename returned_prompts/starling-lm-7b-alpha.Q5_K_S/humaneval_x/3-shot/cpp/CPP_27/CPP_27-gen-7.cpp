    int i;
    char chr;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        if (chr>='a'&&chr<='z')
        chr+=('A'-'a');
        else if (chr>='A'&&chr<='Z')
        chr+=('a'-'A');
        str[i]=chr;
    }
    return str;
}


