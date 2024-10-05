    vector<string> words;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]!=' '&&s[i]!=',')
        {
            words.push_back(s.substr(i, s.find_first_of(" ", i)-i));
            i=s.find_first_of(" ", i);
        }
    }
    return words;
}


