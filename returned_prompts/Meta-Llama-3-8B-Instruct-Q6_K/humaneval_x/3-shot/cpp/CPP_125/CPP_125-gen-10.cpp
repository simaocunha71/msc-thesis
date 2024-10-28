    vector<string> words;
    int i,j;
    for (i=0;i<txt.length();i++)
    {
        if (txt[i]==',')
        {
            words.push_back(txt.substr(i+1));
            i=txt.length();
        }
        else if (txt[i]==' ')
        {
            words.push_back(txt.substr(0,i));
            words.push_back(txt.substr(i+1));
            i=txt.length();
        }
    }
    if (words.size()==0)
    {
        int count=0;
        for (char c : txt)
        {
            if (c>='a' && c<='z' && (int)c-96%2==1)
                count++;
        }
        words.push_back(to_string(count));
    }
    return words;
}