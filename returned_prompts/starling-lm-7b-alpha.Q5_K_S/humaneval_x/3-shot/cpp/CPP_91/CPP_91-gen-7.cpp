    int i,count=0;
    char chr;
    for (i=0;i<S.length();i++)
    {
        chr=S[i];
        if (chr=='.'||chr=='?'||chr=='!')
        {
        if (S[i-1]=='I')
        count+=1;
        }
    }
    return count;
}

