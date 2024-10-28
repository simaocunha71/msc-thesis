    int apples=0,oranges=0;
    int i;
    for (i=0;i<s.length();i++)
    if (s[i]=='a')
    apples++;
    else oranges++;
    return n-apples-oranges;
}


