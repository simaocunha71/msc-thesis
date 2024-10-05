    vector<string> all_words;
    string current_word;
    int level=0;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' ')
        {
            if (current_word.length()>n)
            all_words.push_back(current_word);
            current_word="";
        }
        else
        if (chr=='a' || chr=='e' || chr=='i' || chr=='o' || chr=='u' || chr=='y' || chr=='A' || chr=='E' || chr=='I' || chr=='O' || chr=='U' || chr=='Y')
            ;
        else
        current_word+=chr;
    }
    if (current_word.length()>n)
    all_words.push_back(current_word);
    return all_words;
}



