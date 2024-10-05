    vector<string> words;
    string current_word;
    bool is_word=false;
    for (int i=0;i<txt.length();i++)
    {
        if (txt[i]==' '||txt[i]==',')
        {
            if (is_word)
            {
                words.push_back(current_word);
                current_word="";
                is_word=false;
            }
        }
        else
        {
            is_word=true;
            current_word+=txt[i];
        }
    }
    if (is_word)
    words.push_back(current_word);

    return words;
}


