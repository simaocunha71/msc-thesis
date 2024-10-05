    string result="";
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr>='a' && chr<='z')
        {
            result+=(chr+4);
        }
        if (chr>='A' && chr<='Z')
        {
            result+=(chr+4);
        }
    }
    return result;
}