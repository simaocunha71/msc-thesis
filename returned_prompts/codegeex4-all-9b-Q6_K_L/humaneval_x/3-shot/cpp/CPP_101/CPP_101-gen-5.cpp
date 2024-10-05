    vector<string> all_words;
    string word="";
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==',')
        {
            all_words.push_back(word);
            word="";
        }
        else if (s[i]==' ')
        {
            all_words.push_back(word);
            word="";
        }
        else
        {
            word+=s[i];
        }
    }
    all_words.push_back(word);
    return all_words;
}

