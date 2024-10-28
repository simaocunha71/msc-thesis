    int i;
    for (i=0;i<s.length();i++)
    if (s[i]>='a' && s[i]<='z')
    s[i]=s[i]+'A'-'a';
    else if (s[i]>='A' && s[i]<='Z')
    s[i]=s[i]+'a'-'A';
    return s;
}



