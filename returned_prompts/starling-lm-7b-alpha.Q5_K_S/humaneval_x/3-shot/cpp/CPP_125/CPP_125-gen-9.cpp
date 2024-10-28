    vector<string> words;
    int i;
    for (i=0;i<txt.length();i++)
    if (txt[i]==' '||txt[i]==',')
    {
        words.push_back(txt.substr(0,i));
        txt=txt.substr(i+1);
    }
    if (txt.length()>0)
    words.push_back(txt);
    return words;
}



