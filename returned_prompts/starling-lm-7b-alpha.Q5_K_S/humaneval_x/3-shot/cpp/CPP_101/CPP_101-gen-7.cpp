    vector<string> words;
    char chr;
    string word;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' '||chr==','){
        words.push_back(word);
        word="";
        }
        else
        word+=chr;
    }
    return words;
}



