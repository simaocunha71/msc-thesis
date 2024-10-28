    int bored=0;
    bool word_start=true;
    char chr;
    int i;
    for (i=0;i<S.length();i++)
    {
        chr=S[i];
        if (chr=='.'||chr=='?'||chr=='!')
        word_start=true;
        if (chr==' '||chr=='\t')
        word_start=false;
        if (chr=='I'&&word_start)
        bored+=1;
    }
    return bored;
}


