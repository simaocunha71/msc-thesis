    vector<string> words;
    string word;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' '||chr==',')
        {
            if (word!="")
            words.push_back(word);
            word="";
        }
        else
        word+=chr;
    }
    words.push_back(word);
    return words;
}


