    vector<string> words;
    vector<char> spaces;
    vector<char> commas;
    for (int i=0;i<txt.length();i++)
    {
        if (txt[i]==' ')
        spaces.push_back(txt[i]);
        if (txt[i]==',')
        commas.push_back(txt[i]);
    }
    if (spaces.size()!=0)
    {
        for (int i=0;i<txt.length();i++)
        {
            if (i==spaces[0])
            {
                words.push_back(txt.substr(i,i+1));
                spaces.erase(spaces.begin());
            }
        }
    }
    if (commas.size()!=0)
    {
        for (int i=0;i<txt.length();i++)
        {
            if (i==commas[0])
            {
                words.push_back(txt.substr(i,i+1));
                commas.erase(commas.begin());
            }
        }
    }
    if (spaces.size()==0 && commas.size()==0)
    {
        int odd=0;
        for (int i=0;i<txt.length();i++)
        {
            if (txt[i]>='a' && txt[i]<='z')
            {
                if (i%2!=0)
                odd++;
            }
        }
        words.push_back(odd);
    }
    return words;
}


