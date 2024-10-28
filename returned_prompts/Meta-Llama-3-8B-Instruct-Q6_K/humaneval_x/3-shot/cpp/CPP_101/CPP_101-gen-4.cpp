    vector<string> words;
    string current_word;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' ' || s[i]==',')
        {
            if (!current_word.empty())
            {
                words.push_back(current_word);
                current_word="";
            }
        }
        else
        {
            current_word+=s[i];
        }
    }
    if (!current_word.empty())
    {
        words.push_back(current_word);
    }
    return words;
}  