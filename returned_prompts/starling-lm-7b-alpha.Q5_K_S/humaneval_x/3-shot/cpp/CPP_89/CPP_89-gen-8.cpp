    int i;
    string res="";
    for (i=0;i<s.length();i++)
    {
        char chr=s[i];
        if (chr>='a' && chr<='z')
        {
        chr+=2;
        chr+=2;
        if (chr>'z')
        chr-=26;
        res+=chr;
        }
        else
        if (chr>='A' && chr<='Z')
        {
        chr+=2;
        chr+=2;
        if (chr>'Z')
        chr-=26;
        res+=chr;
        }
        else
        res+=chr;
    }
    return res;
}


