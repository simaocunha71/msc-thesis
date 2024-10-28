    int i;
    char chr;
    string result="";
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        if (chr>='A'&&chr<='Z')
        result+=chr+32;
        if (chr>='a'&&chr<='z')
        result+=chr-32;
    }
    return result;
}

