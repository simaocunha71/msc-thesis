    vector<string> words;
    string word;
    int i;
    for (i=0;i<s.length();i++)
    {
        char chr=s[i];
        if (chr==',')
        {
            words.push_back(word);
            word="";
        }
        else if (chr==' ')
        {
            if (word.length()>0)
            {
            words.push_back(word);
            word="";
            }
        }
        else
        {
            word+=chr;
        }
    }
    if (word.length()>0)
    {
        words.push_back(word);
    }
    return words;
}

