    vector<string> words;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' '||chr==',')
        {
            if (i>0)
            words.push_back(s.substr(0,i));
            s=s.substr(i+1);
            i=0;
        }
    }
    words.push_back(s);
    return words;
}


