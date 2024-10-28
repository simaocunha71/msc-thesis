    int i;
    for (i=0;i<s.length();i++)
    if (s[i]>='a' && s[i]<='z')
    s[i]=s[i]-'a'+'A';
    else if (s[i]<='Z' && s[i]>='A')
    s[i]=s[i]-'A'+'a';

    return s;
}



