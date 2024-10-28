    vector<string> words;
    string current_word;
    int i;
    for (i=0;i<txt.length();i++)
    {
        char chr=txt[i];
        if (chr==',' || chr==' ')
        {
            if (!current_word.empty())
            {
                words.push_back(current_word);
                current_word="";
            }
        }
        else
        {
            current_word+=chr;
        }
    }
    if (!current_word.empty())
    {
        words.push_back(current_word);
    }
    else
    {
        int count=0;
        for (char c='a';c<='z';c++)
        {
            if (count%2!=0)
            {
                count++;
                continue;
            }
            if (txt.find(c)!=string::npos)
                return {to_string(count)};
        }
    }
    return words;
} 