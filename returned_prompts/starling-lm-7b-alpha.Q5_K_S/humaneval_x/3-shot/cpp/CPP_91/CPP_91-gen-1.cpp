    int i,boredom_count=0;
    char chr;
    for (i=0;i<S.length();i++)
    {
        chr=S[i];
        if (chr=='.')
        {
            if (S[i-1]=='I')
            {
                boredom_count+=1;
            }
        }
        if (chr=='?')
        {
            if (S[i-1]=='I')
            {
                boredom_count+=1;
            }
        }
        if (chr=='!')
        {
            if (S[i-1]=='I')
            {
                boredom_count+=1;
            }
        }
    }
    return boredom_count;
}


