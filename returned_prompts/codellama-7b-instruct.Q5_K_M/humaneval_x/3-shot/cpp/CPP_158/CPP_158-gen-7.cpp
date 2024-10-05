    sort(words.begin(),words.end());
    int size=words[0].length();
    for (int i=1;i<words.size();i++)
    {
        if (words[i].length()>size)
        {
        size=words[i].length();
        }
    }
    int k=0;
    for (int i=0;i<words.size();i++)
    {
        if (words[i].length()==size)
        {
            return words[i];
        }
    }
}

