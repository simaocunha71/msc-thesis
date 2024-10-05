    vector<string> result;
    string word;
    int consonants=0;
    for (int i=0;i<s.length();i++)
    {
        if (isalpha(s[i]))
        {
            word+=tolower(s[i]);
            if (s[i] != 'a' && s[i] != 'e' && s[i] != 'i' && s[i] != 'o' && s[i] != 'u')
            {
                consonants++;
            }
        }
        else if (s[i] == ' ')
        {
            if (consonants == n)
            {
                result.push_back(word);
            }
            word.clear();
            consonants=0;
        }
    }
    if (consonants == n)
    {
        result.push_back(word);
    }
    sort(result.begin(),result.end());
    return result;
}

