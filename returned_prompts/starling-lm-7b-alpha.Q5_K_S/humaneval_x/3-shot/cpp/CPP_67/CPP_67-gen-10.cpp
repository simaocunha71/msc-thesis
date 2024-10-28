    int i;
    int apple=0;
    int orange=0;
    int mango=0;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='a')
        {
            apple+=1;
        }
        if (s[i]=='o')
        {
            orange+=1;
        }
    }
    mango=n-(apple+orange);
    return mango;
}


