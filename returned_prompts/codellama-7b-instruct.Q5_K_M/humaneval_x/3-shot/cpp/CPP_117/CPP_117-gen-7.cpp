    vector<string> words;
    vector<string>::iterator it;
    int count;
    int i;
    int size;
    string word;
    for (i=0;i<s.size();i++)
    {
        if (s[i]!=' ')
        {
            word="";
            word+=s[i];
            size=word.size();
            count=0;
            for (it=word.begin();it!=word.end();it++)
            {
                if (!isalpha(*it))
                {
                    continue;
                }
                if (!islower(*it))
                {
                    *it=tolower(*it);
                }
                if (isalpha(*it) && *it!='a' && *it!='e' && *it!='i' && *it!='o' && *it!='u')
                {
                    count++;
                }
            }
            if (count==n)
            {
                words.push_back(word);
            }
        }
    }
    return words;
}


