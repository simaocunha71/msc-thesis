    vector<string> words;
    string word="";
    int i;
    for (i=0;i<txt.length();i++)
    {
        if (txt[i]==' '||txt[i]==',')
        {
            if (word!="")
            {
                words.push_back(word);
                word="";
            }
        }
        else if (txt[i]>='a'&&txt[i]<='z')
        {
            word+=txt[i];
        }
    }
    if (word!="")
    {
        words.push_back(word);
        word="";
    }
    return words;
}



