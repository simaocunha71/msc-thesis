    int i,j;
    char chr;
    string res="";
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr<='z')
        {
        chr+=2;
        if (chr>'z')
        chr-=26;
        }
        else if (chr<='Z')
        {
        chr+=2;
        if (chr>'Z')
        chr-=26;
        }
        res+=chr;
    }
    return res;
}



