    vector<string> all_words;
    string current_word;
    int i;
    for (i=0;i<txt.length();i++)
    {
        char chr=txt[i];
        if (chr==' ')
        {
            all_words.push_back(current_word);
            current_word="";
        }
        else if (chr==',')
        {
            all_words.push_back(current_word);
            current_word="";
        }
        else
        {
            current_word+=chr;
        }
    }
    if (current_word!="")
    all_words.push_back(current_word);
    else{
        int sum=0;
        for (i=0;i<txt.length();i++)
        {
            chr=txt[i];
            if (chr>='a'&&chr<='z')
            {
                if ((chr-'a')%2!=0)
                sum+=1;
            }
        }
        all_words.push_back(to_string(sum));
    }
    return all_words;
}

