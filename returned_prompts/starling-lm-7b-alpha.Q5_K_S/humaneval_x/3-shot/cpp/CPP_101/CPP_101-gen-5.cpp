    vector<string> all_words;
    string word="";
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' '|| s[i]==','){
            all_words.push_back(word);
            word="";
        }
        else
        {
            word+=s[i];
        }
    }
    return all_words;
}


