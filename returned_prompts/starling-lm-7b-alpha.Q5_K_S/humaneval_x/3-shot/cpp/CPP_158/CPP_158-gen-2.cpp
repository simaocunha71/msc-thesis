    int i;
    string max_word;
    int max_len=0;
    for (i=0;i<words.size();i++)
    {
        if (words[i].length()>max_len)
        {
            max_word=words[i];
            max_len=words[i].length();
        }
    }

    char chr;
    int j;
    int len=0;
    for (i=0;i<words.size();i++)
    if (words[i]==max_word)
    {
        for (j=0;j<words[i].length();j++)
        {
            chr=words[i][j];
            if (find(unique(max_word.begin(),max_word.end()),chr)==unique(max_word.begin(),max_word.end()))
            {
                len+=1;
            }
        }
    }
    if (len<max_len)
        return find_max(words);
    return max_word;
}




