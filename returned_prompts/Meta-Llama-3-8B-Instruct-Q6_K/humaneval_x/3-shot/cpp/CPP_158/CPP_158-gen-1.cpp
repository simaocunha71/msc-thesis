    string max_word;
    int max_unique_chars=0;
    for (auto word: words)
    {
        if (word.size()>max_unique_chars)
        {
            max_word=word;
            max_unique_chars=word.size();
        }
        else if (word.size()==max_unique_chars)
        {
            if (word<max_word)
            {
                max_word=word;
            }
        }
    }
    return max_word;
}