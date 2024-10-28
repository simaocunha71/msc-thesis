    int i;
    char chr;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        if (chr>=97 && chr<=122)
        chr+=41;
        else if (chr>=65 && chr<=90)
        chr+=(32);
        str[i]=chr;
    }
    return str;
}


