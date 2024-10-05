    string e="";
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]>='a' && s[i]<='z')
        e+=char(s[i]-2*(s[i]-'a'));
        else if (s[i]>='A' && s[i]<='Z')
        e+=char(s[i]-2*(s[i]-'A'));
    }
    return e;
}








