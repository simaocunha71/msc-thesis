    vector<string> words;
    string current_word;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' '||chr==',')
        {
            if (current_word.length()!=0)
            words.push_back(current_word);
            current_word="";
        }
        else current_word+=chr;
    }
    words.push_back(current_word);
    return words;
}


