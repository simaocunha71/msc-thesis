    string ans;
    string chr;
    int i,j;
    for (i=0;i<s.length();i++)
    if (s[i]!=' ')
    {
        chr=s[i];
        for (j=i+1;j<s.length();j++)
        if (s[j]<chr)
        chr=s[j];
        ans+=chr;
        i=j-1;
    }
    return ans;
}

