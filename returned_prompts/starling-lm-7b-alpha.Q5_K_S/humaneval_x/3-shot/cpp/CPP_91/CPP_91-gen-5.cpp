    int i=0,cnt=0;
    while (i<S.length())
    {
        if (S[i]=='I')
        {
            cnt+=1;
            while (S[i]!='.')
            {
                i+=1;
            }
            i+=1;
        }
        else
        {
            while (S[i]!=('.')&&S[i]!=('?')&&S[i]!=('!'))
            {
                i+=1;
            }
            i+=1;
        }
    }
    return cnt;
}


