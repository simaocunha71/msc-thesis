    int i;
    for (i=0;i<s.length();i++)
    if (isalpha(s[i]))
    if (islower(s[i]))
    s[i]=toupper(s[i]);
    else
    s[i]=tolower(s[i]);

    if (isalpha(s[i])==false)
    {
    string s2="";
    for (i=s.length()-1;i>=0;i--)
    s2+=s[i];
    return s2;
    }

    return s;
}

