    vector<string> words;
    string current_word;
    int i;
    for (i=0;i<txt.length();i++)
    {
        if (txt[i]==' ')
        {
            if (current_word.length()>0)
            {
                words.push_back(current_word);
                current_word="";
            }
        }
        else if (txt[i]==',')
        {
            if (current_word.length()>0)
            {
                words.push_back(current_word);
                current_word="";
            }
        }
        else
        {
            current_word+=txt[i];
        }
    }
    if (current_word.length()>0)
    {
        words.push_back(current_word);
    }
    else
    {
        int count=0;
        for (i=0;i<current_word.length();i++)
        {
            if (current_word[i]-'a' % 2 != 0)
            {
                count++;
            }
        }
        words.push_back(to_string(count));
    }
    return words;
}