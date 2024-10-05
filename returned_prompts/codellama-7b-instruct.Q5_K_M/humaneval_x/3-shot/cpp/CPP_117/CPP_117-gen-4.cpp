    vector<string> all_words;
    string word;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]!=' ')
        {
            word+=s[i];
        }
        else
        {
            if (word.length()==n)
            {
                all_words.push_back(word);
            }
            word="";
        }
    }
    return all_words;
}



