    int i;
    for (i=0;i<str.length();i++)
    {
        char chr=str[i];
        if (chr>=65&&chr<=90)
        str[i]=chr+32;
        if (chr>=97&&chr<=122)
        str[i]=chr-32;
    }
    return str;
}

