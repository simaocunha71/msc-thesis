    string result;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        sort(chr);
        result+=chr;
    }
    return result;
}



