    vector<string> words;
    char chr;
    int i;
    for (i=0;i<txt.length();i++)
    {
        chr=txt[i];
        if (chr==' '||chr==','||chr=='\0')
        {
            words.push_back("");
        }
        else
        {
            words[words.size()-1]+=chr;
        }
    }
    return words;
}



