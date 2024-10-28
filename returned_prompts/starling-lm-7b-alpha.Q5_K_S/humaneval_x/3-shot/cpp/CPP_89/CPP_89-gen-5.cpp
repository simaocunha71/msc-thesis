    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]>='a' && s[i]<='z')
        s[i]=char(122-2*(s[i]-97));
        else if (s[i]>='A' && s[i]<='Z')
        s[i]=char(90-2*(s[i]-65));
    }
    return s;
}



