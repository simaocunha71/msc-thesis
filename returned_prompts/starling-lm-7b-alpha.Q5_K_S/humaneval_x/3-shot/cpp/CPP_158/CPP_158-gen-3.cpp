    int i;
    int max_len=0;
    string max_word;
    for (i=0;i<words.size();i++)
    {
        string word=words[i];
        int len=word.length();
        int curr_len=0;
        for (char c='a';c<='z';c++)
        {
            int ind=word.find(c);
            if (ind!=string::npos)
            {
            curr_len+=1;
            }
        }
        if (curr_len>max_len)
        {
            max_word=word;
            max_len=curr_len;
        }
        else if (curr_len==max_len && word<max_word)
        {
            max_word=word;
        }
    }
    return max_word;
}


