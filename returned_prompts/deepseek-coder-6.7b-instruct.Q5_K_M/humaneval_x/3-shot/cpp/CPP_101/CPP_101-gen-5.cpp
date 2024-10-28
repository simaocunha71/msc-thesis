    vector<string> words;
    string word="";
    int i;
    for(i=0;i<s.length();i++)
    {
        if(s[i]==' '||s[i]==',')
        {
            if(word.length()>0)
            {
                words.push_back(word);
                word="";
            }
        }
        else
        {
            word+=s[i];
        }
    }
    if(word.length()>0)
    {
        words.push_back(word);
    }
    return words;
}


