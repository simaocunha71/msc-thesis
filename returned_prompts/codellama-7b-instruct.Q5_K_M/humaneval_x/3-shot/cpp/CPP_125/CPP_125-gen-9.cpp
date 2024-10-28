    vector<string> words;
    int i;
    bool comma=false;
    int j;
    for (i=0;i<txt.length();i++)
    {
        if (txt[i]==',')
        {
            comma=true;
        }
        if ((txt[i]==' ')||(comma))
        {
            words.push_back(txt.substr(j,i-j));
            comma=false;
            j=i+1;
        }
    }
    words.push_back(txt.substr(j,i-j));
    return words;
}



