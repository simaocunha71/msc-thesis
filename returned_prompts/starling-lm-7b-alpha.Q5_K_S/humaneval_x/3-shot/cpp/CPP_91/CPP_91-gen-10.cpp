    int i=0;
    char chr;
    int count=0;
    while (i<S.length())
    {
        chr=S[i];
        if (chr=='I')
        {
            if (i+1<S.length() && (S[i+1]=='.' || S[i+1]=='?' || S[i+1]=='!' ))
            count+=1;
        }
        i+=1;
    }
    return count;
}




