    int i,count=0;
    for (i=0;i<S.length();i++)
    if (S[i]=='.'||S[i]=='?'||S[i]=='!')
    {
        if (S[i-1]=='I')
        count+=1;
    }
    return count;
}



