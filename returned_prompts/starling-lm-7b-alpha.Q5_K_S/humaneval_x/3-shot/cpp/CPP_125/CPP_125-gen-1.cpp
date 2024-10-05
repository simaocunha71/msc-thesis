    int i,j;
    for (i=0;i<txt.length();i++)
    if (txt[i]==' ')
    {
        txt.insert(i+1,'|');
    }
    for (i=0;i<txt.length();i++)
    if (txt[i]==',' || txt[i]=='|')
    {
        txt.erase(i,'|');
        txt.erase(i,',');
    }
    vector<string> words;
    for (i=0;i<txt.length();i++)
    {
        if (txt[i]==' ')
        {
            string word;
            for (j=i+1;j<txt.length();j++)
            if (txt[j]!=' ')
            {
                word+=txt[j];
            }
            words.push_back(word);
        }
    }
    return words;
}



