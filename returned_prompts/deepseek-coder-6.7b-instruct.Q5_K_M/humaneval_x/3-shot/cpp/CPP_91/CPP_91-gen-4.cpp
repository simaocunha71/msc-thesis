    int count = 0;
    string word = "";
    for (int i = 0; i < S.size(); i++)
    {
        if (S[i] == ' ' || S[i] == '.' || S[i] == '?' || S[i] == 'A' || S[i] == 'a')
        {
            if(word == "I") count++;
            word = "";
        }
        else
            word += S[i];
    }
    return count;
}

