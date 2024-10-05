    int i;
    for (i=0;i<s.length();i++)
    if (isalpha(s[i]))
    s[i]=islower(s[i])?toupper(s[i]):tolower(s[i]);
    return s;
}


