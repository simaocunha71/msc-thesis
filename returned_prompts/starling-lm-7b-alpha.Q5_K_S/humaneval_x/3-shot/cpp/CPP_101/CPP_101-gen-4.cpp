    vector<string> all_words;
    int i=0;
    while (i<s.length())
    {
        if (s[i]==' '||s[i]==',')
        {
            all_words.push_back(s.substr(i-1,2));
            i+=2;
        }
        else
        {
            all_words.push_back(s.substr(i,1));
            i+=1;
        }
    }
    return all_words;
}



