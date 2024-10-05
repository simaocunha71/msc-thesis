    vector<string> all_words;
    string current_word;
    int i;
    for (i=0;i<txt.length();i++)
    {
        if (txt[i]==' ')
        {
            all_words.push_back(current_word);
            current_word="";
        }
        if (txt[i]==',')
        {
            all_words.push_back(current_word);
            current_word="";
        }
        else
        {
            current_word+=txt[i];
        }
    }
    if (current_word.length()!=0)
        all_words.push_back(current_word);

    if (all_words.size()==0)
    {
        int count=0;
        for (int i=0;i<txt.size();i++)
        {
            if (txt[i]>=97 && txt[i]<=122)
            {
                if (txt[i]%2!=0)
                    count+=1;
            }
        }
        string s;
        s+=count;
        all_words.push_back(s);
    }
    return all_words;
}

