    int i;
    char chr;
    string ans="";
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr>='a' && chr<='z')
        ans+=chr-32;
        else if (chr>='A' && chr<='Z')
        ans+=chr+32;
        else
        ans+=chr;
    }
    return ans;
}


