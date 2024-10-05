    int i,apples,oranges;
    char chr;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='a')
        {
            while (i<s.length() && s[i]=='p') i++;
            apples=i-1;
        }
        if (s[i]=='o')
        {
            while (i<s.length() && s[i]=='r') i++;
            oranges=i-1;
        }
    }
    return n-apples-oranges;
}


