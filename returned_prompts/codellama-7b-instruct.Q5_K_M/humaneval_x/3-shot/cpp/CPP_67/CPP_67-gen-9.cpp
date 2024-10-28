    int apples=0;
    int oranges=0;
    int i;
    for (i=0;i<s.length();i++)
    {
    if (s[i]=='a')
    apples++;
    if (s[i]=='o')
    oranges++;
    }
    return n-apples-oranges;
}


