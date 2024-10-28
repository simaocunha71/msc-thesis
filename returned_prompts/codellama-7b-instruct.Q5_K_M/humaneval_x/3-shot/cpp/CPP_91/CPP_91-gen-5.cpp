    int count=0;
    char chr;
    int i;
    for (i=0;i<S.length();i++)
    {
        chr=S[i];
        if (chr=='I' && (S[i+1]=='.' || S[i+1]=='?' || S[i+1]=='!'))
        count+=1;
    }
    return count;
}


