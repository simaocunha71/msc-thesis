    int apples=0, oranges=0, mango=0;
    int i, j;
    for (i=0;i<s.length();i++)
    if (s[i]=='a')
    apples++;
    else
    oranges++;
    mango=n-apples-oranges;
    return mango;
}


