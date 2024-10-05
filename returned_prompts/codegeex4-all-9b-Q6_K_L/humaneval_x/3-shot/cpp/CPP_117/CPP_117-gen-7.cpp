    vector<string> all_words;
    string current_word="";
    int i;
    int consonants=0;
    int spaces=0;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' ')
        {
            consonants=0;
            spaces=0;
            if (current_word.length()>0)
            {
            all_words.push_back(current_word);
            current_word="";
            }
            continue;
        }
        else
        {
            if (chr=='a' || chr=='e' || chr=='i' || chr=='o' || chr=='u' || chr=='A' || chr=='E' || chr=='I' || chr=='O' || chr=='U')
            continue;
            consonants+=1;
        }
        current_word+=chr;
    }
    if (current_word.length()>0)
    {
    all_words.push_back(current_word);
    }
    vector<string> filtered_words;
    for (i=0;i<all_words.size();i++)
    {
        if (consonants==n)
        filtered_words.push_back(all_words[i]);
    }
    return filtered_words;
}

