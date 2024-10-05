    vector<string> words;
    string word;
    for (int i=0;i<s.length();i++)
    {
        if (s[i]>='a' && s[i]<='z' || s[i]>='A' && s[i]<='Z')
        {
            word+=s[i];
        }
        else if (word.length()>0)
        {
            int consonants=0;
            for (int j=0;j<word.length();j++)
            {
                if (word[j]!='a' && word[j]!='e' && word[j]!='i' && word[j]!='o' && word[j]!='u' && word[j]!='A' && word[j]!='E' && word[j]!='I' && word[j]!='O' && word[j]!='U')
                {
                    consonants++;
                }
            }
            if (consonants==n)
            {
                words.push_back(word);
            }
            word="";
        }
    }
    if (word.length()>0)
    {
        int consonants=0;
        for (int j=0;j<word.length();j++)
        {
            if (word[j]!='a' && word[j]!='e' && word[j]!='i' && word[j]!='o' && word[j]!='u' && word[j]!='A' && word[j]!='E' && word[j]!='I' && word[j]!='O' && word[j]!='U')
            {
                consonants++;
            }
        }
        if (consonants==n)
        {
            words.push_back(word);
        }
    }
    sort(words.begin(),words.end());
    return words;
} // O(NM) time complexity, where N is the number of words and M is the average length of a word. This is because we are iterating over each character of each word. The space complexity is O(N) as we are storing the words in a vector.