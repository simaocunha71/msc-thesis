    int i,level;
    level=0;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='I')
        {
            level+=1;
        }
    }
    return level;
}

