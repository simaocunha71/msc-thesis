    vector<string> words;
    string word;
    int i;
    for (i=0;i<txt.length();i++)
    {
        if (txt[i]==' '||txt[i]==',')
        {
            words.push_back(word);
            word="";
        }
        else
        word+=txt[i];
    }
    words.push_back(word);
    return words;
}


