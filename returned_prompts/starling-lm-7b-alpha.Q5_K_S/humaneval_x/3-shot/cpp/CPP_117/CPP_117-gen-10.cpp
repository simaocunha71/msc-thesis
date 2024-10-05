    vector<string> all_words;
    char chr;
    int level=0;
    string current_word="";
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' '){
            if (level==n)
            all_words.push_back(current_word);
            current_word="";
            level=0;
        }
        if (isalpha(chr)){
        if (isconsonant(chr))
            level+=1;
        current_word+=chr;
        }
    }
    if (level==n)
    all_words.push_back(current_word);
    return all_words;
}


