    int count=0;
    string word;
    int i;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='I')
        {
            count+=1;
            i+=1;
            while (S[i]!=' ')
            i+=1;
        }
        if (S[i]=='.'||S[i]=='?'||S[i]=='!')
            i+=1;
    }
    return count;
}

