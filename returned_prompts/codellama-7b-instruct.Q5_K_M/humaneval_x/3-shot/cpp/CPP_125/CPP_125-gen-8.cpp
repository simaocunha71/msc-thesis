    vector<string> all_words;
    string current_word;
    int level=0;
    char chr;
    int i;
    for (i=0;i<txt.length();i++)
    {
        chr=txt[i];
        if (chr==' '||chr==',')
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




