    vector<string> all_words;
    char chr;
    for (int i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' '||chr==',')
        {
            all_words.push_back("" + s.substr(i-1, 1));
        }
    }
    return all_words;
}


