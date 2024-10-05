    string max_word;
    int max_unique_chars=0;
    for (string word:words)
    {
        set<char> unique_chars(word.begin(),word.end());
        if (unique_chars.size()>max_unique_chars)
        {
            max_unique_chars=unique_chars.size();
            max_word=word;
        }
        else if (unique_chars.size()==max_unique_chars)
        {
            if (word<max_word)
                max_word=word;
        }
    }
    return max_word;
}