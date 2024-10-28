    vector<string> words;
    string curr_word;
    int i;
    int count=0;
    bool word=false;
    for (i=0;i<s.length();i++)
    {
        char chr=s[i];
        if (chr==' ')
        {
            if (word==true)
            {
                word=false;
                if (count==n)
                words.push_back(curr_word);
                curr_word="";
                count=0;
            }
        }
        else
        {
            if (word==false)
            {
            word=true;
            curr_word+=chr;
            }
            else
            {
            curr_word+=chr;
            if (chr!='a' && chr!='e' && chr!='i' && chr!='o' && chr!='u')
            count+=1;
            }
        }
    }
    return words;
}

