    int i,count=0;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='a'||s[i]=='o')
        count++;
    }
    return n-count;
}


