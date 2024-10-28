    vector<string> words;
    string word;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' '||s[i]==',')
        {
            words.push_back(word);
            word="";
        }
        else
        word+=s[i];
    }
    words.push_back(word);
    return words;
}


