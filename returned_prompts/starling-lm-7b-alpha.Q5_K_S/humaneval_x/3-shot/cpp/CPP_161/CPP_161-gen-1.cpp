    int i;
    int len=s.length();
    for (i=0;i<len;i++)
    if (s[i]>='a' && s[i]<='z')
        s[i]=char(s[i]-'a'+'A');
    else if (s[i]>='A' && s[i]<='Z')
        s[i]=char(s[i]-'A'+'a');
    return s;
}



