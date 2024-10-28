    int i,boredoms=0;
    char chr;
    for (i=0;i<S.length();i++)
    {
        chr=S[i];
        if (chr=='I')
        {
            while (i<S.length() && S[i]==' ')
            i+=1;
            if (i<S.length() && (S[i]=='.'||S[i]=='?'||S[i]=='!'))
            boredoms+=1;
        }
    }
    return boredoms;
}


