    int i;
    for (i=0;i<s.length();i++)
    {
        if (i%3==0 && i+2<s.length())
        {
            if (s[i+2]>s[i]) s[i]='0';
            else s[i]='1';
        }
        if (s[i]=='1') s[i]='0';
        else s[i]='1';
    }
    return s;
}

