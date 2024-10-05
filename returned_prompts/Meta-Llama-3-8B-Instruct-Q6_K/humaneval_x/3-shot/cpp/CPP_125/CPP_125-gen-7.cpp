    vector<string> words;
    string current_word;
    int i;
    for (i=0;i<txt.length();i++)
    {
        if (ispunct(txt[i]) || isdigit(txt[i]))
        {
            if (current_word.length()>0)
            {
                words.push_back(current_word);
                current_word="";
            }
        }
        else if (isspace(txt[i]))
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
        for (int j=0;j<26;j++)
        {
            if (txt.find((char)(j+'a')) != string::npos)
                count++;
        }
        words.push_back(to_string(count));
    }
    return words;
}  // end of function split_words


