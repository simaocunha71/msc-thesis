    int i,j;
    int count=0;
    string sentence;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='.' || S[i]=='?' || S[i]=='!')
        {
            sentence=S.substr(j,i-j);
            if (sentence.find("I")!=string::npos)
            count++;
            j=i+1;
        }
    }
    return count;
}


