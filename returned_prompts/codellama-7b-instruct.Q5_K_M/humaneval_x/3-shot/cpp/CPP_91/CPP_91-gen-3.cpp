    int i;
    int count=0;
    string current_sentence;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='.'||S[i]=='!'||S[i]=='?')
        {
        if (current_sentence[0]=='I')
        count+=1;
        current_sentence="";
        }
        else
        current_sentence+=S[i];
    }
    if (current_sentence[0]=='I')
    count+=1;
    return count;
}


