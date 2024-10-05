    vector<string> all_words;
    string current_word="";
    int i;
    for (i=0;i<txt.length();i++)
    {
        if (txt[i]==' '||txt[i]==',')
        {
            if (current_word.length()>0)
            all_words.push_back(current_word);
            current_word="";
        }
        else current_word+=txt[i];
    }
    if (current_word.length()>0)
    all_words.push_back(current_word);
    return all_words;
}


