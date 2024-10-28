    vector<string> words;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' '||chr==',')
        {
            words.push_back(""+s.substr(i-1,2));
        }
    }
    return words;
}


