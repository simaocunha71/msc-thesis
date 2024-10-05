    int apples,oranges;
    char chr;
    int i;
    apples=0;
    oranges=0;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr=='a')
        {
        apples+=1;
        }
        if (chr=='o')
        {
        oranges+=1;
        }
    }
    return n-apples-oranges;
}



