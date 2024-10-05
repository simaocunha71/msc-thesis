    string max_word=words[0];
    int max_chars=words[0].length();
    int i;
    for (i=0;i<words.size();i++)
    {
        if (words[i].length()>max_chars){
            max_chars=words[i].length();
            max_word=words[i];
        }
    }
    sort(words.begin(), words.end());
    for (i=0;i<words.size();i++)
    {
        if (words[i].length()==max_chars && words[i]<max_word)
        max_word=words[i];
    }
    return max_word;
}


