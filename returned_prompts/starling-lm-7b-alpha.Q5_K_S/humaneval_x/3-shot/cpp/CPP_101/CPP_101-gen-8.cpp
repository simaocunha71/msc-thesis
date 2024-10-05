    vector<string> all_words;
    int i;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' ' || chr==',')
        {
            all_words.push_back(s.substr(last_index(s,' '),i-last_index(s,' ')));
        }
    }
    return all_words;
}


