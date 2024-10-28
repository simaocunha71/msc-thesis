    int i;
    int max_length=0;
    string max_word;
    for (i=0;i<words.size();i++)
    {
        if (max_length<words[i].length())
        {
            max_length=words[i].length();
            max_word=words[i];
        }
    }
    vector<int> unique_chars;
    for (i=0;i<max_word.length();i++)
    {
        int index;
        index=max_word.find(max_word[i],i+1);
        if (index>i+1)
        {
            unique_chars.push_back(max_word[i]);
        }
    }
    if (unique_chars.size()>max_length)
    {
        return max_word;
    }
    return max_word;
}


