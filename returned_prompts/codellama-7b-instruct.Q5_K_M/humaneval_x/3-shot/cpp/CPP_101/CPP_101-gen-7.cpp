    vector<string> words;
    int i=0;
    string word;
    char chr;
    while (s[i]!='\0')
    {
        chr=s[i];
        if (chr==' '||chr==',')
        {
        words.push_back(word);
        word="";
        }
        else
        word+=chr;
        i++;
    }
    words.push_back(word);
    return words;
}

