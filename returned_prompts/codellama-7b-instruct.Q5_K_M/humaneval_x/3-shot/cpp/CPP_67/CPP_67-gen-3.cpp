    int apples=0;
    int oranges=0;
    int mango=0;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='a')
        apples+=1;
        if (s[i]=='o')
        oranges+=1;
    }
    return n-apples-oranges;
}


