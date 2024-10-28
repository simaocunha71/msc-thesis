    vector<string> all_words;
    string current_word="";
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==',')
        {
            all_words.push_back(current_word);
            current_word="";
        }
        if (chr==' ')
        {
            all_words.push_back(current_word);
            current_word="";
        }
        else
            current_word+=chr;
    }
    if (current_word!="")
        all_words.push_back(current_word);
    return all_words;
}

