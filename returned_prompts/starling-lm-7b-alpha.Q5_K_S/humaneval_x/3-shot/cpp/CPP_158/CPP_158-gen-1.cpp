    string max_word;
    int max_len=0;
    int i;
    for (i=0;i<words.size();i++)
    {
    int len=words[i].length();
    int j;
    for (j=0;j<len;j++)
    {
        if (!(find(max_word.begin(),max_word.end(),words[i][j])!=max_word.end()))
        {
        max_word+=words[i][j];
        }
    }
    if (max_len<max_word.length())
    {
        max_len=max_word.length();
        max_word=words[i];
    }
    }
    return max_word;
}




