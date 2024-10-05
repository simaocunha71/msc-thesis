    vector<string> all_words;
    string current_word;
    int i;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==',')
        {
            all_words.push_back(current_word);
            current_word="";
        }
        else if (chr==' ')
        {
            all_words.push_back(current_word);
            current_word="";
        }
        else{
            current_word+=chr;
        }
    }
    all_words.push_back(current_word);
    return all_words;
}

