    vector<string> words;
    vector<string> vowels{"a","e","i","o","u"};
    int i;
    string word;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' ')
        {
            if (word.length()==n)
            {
                words.push_back(word);
            }
            word="";
        }
        else
        {
            if (find(vowels.begin(),vowels.end(),word)==vowels.end())
            {
                word+=s[i];
            }
        }
    }
    return words;
}

