    vector<string> words;
    string word="";
    int i;
    int count=0;
    for  (i=0;i<txt.length();i++)
    {
        if  (txt[i]==' '||txt[i]==',')
        {
            if  (word.length()>0)
            {
                words.push_back(word);
            }
            word="";
        }
        else
        {
            word+=txt[i];
            if  (islower(txt[i])&&(int(txt[i])-int('a'))%2==1)
            {
                count++;
            }
        }
    }
    if  (word.length()>0)
    {
        words.push_back(word);
    }
    if  (count>0)
    {
        words.push_back(to_string(count));
    }
    return words;
}


