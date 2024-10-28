    vector<string> words;
    string word;
    int i,j;
    for (i=0;i<s.length();i++)
    {
        if (s[i]!=' ')
        {
        word+=s[i];
        }
        else
        {
        if (word.length()==n)
        words.push_back(word);
        word="";
        }
    }
    if (word.length()==n)
    words.push_back(word);
    return words;
}


