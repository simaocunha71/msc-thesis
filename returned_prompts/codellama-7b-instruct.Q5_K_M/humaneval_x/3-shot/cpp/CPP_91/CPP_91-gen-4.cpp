    int count=0;
    string sentence;
    int i;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='.'||S[i]=='?'||S[i]=='!')
        {
        sentence=S.substr(0,i);
        if (sentence[0]=='I')
        count+=1;
        }
    }
    return count;
}


