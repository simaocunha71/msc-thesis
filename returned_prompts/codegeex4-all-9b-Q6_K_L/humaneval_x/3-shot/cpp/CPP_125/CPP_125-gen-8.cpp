    vector<string> words;
    string current_word="";
    int i;
    int counter=0;
    for (i=0;i<txt.length();i++)
    {
        if (txt[i]==' ')
        {
            if (current_word.length()>0)
            words.push_back(current_word);
            current_word="";
        }
        else if (txt[i]==',')
        {
            if (current_word.length()>0)
            words.push_back(current_word);
            current_word="";
        }
        else
        {
            if (txt[i]>='a' && txt[i]<='z')
            {
                if ((txt[i]-97)%2==1)
                counter+=1;
            }
            current_word+=txt[i];
        }
    }
    if (current_word.length()>0)
    words.push_back(current_word);
    if (words.size()==0)
    {
        string str="";
        str+=counter;
        words.push_back(str);
    }
    return words;
}

