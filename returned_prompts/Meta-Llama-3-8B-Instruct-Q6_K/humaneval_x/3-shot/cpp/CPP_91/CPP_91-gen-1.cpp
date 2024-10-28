    int boredoms=0;
    string sentence;
    char chr;
    int i;
    for (i=0;i<S.length();i++)
    {
        chr=S[i];
        if (chr=='.'||chr=='?'||chr== '!'){
            if (sentence.length()>0 && sentence[0] == 'I')
                boredoms++;
            sentence="";
        }
        else{
            sentence+=chr;
        }
    }
    if (sentence.length()>0 && sentence[0] == 'I')
        boredoms++;
    return boredoms;
}