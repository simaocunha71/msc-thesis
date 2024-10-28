    int i;
    int n=0;
    int count=0;
    for (i=0;i<S.length();i++)
    if (S[i]=='.'||S[i]=='?'||S[i]=='!')
    {
        count+=1;
        n=0;
    }
    else if (S[i]=='I')
    {
        n+=1;
        if (count==n)
        return 1;
    }
    return 0;
}


