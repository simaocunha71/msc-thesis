    int count=0;
    string sentence;
    for (int i=0;i<S.length();i++)
    {
        if (S[i]=='.' || S[i]=='?' || S[i]=='!')
        {
            if (sentence.find("I") != string::npos)
            {
                count++;
            }
            sentence="";
        }
        else
        {
            sentence+=S[i];
        }
    }
    if (sentence.find("I") != string::npos)
    {
        count++;
    }
    return count;
}

