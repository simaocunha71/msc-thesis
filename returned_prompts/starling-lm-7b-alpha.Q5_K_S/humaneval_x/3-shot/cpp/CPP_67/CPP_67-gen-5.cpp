    int i,count,a,o;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr=='a')
        {
            count+=1;
        }
        if (chr=='o')
        {
            count+=1;
        }
    }
    a=count;
    count=0;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr=='a')
        {
            count+=1;
        }
        if (chr=='o')
        {
            count+=1;
        }
    }
    o=count;
    return n-a-o;
}


