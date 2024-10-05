    int i,a,o,m;
    int length=s.length();
    a=0;
    o=0;
    m=n-a-o;
    for (i=0;i<length;i++)
    {
        if (s[i]=='a')
        a+=1;
        else if (s[i]=='o')
        o+=1;
        else if (s[i]=='m')
        m+=1;
    }
    return m;
}


