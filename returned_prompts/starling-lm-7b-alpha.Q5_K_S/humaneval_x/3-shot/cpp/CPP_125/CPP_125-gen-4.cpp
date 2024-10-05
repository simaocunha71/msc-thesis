    vector<string> all_words;
    string word;
    char chr;
    int i;
    for (i=0;i<txt.length();i++)
    {
        chr=txt[i];
        if (chr==' ' || chr==',' || chr=='\0')
        {
            if (word.length()!=0)
            all_words.push_back(word);
            word="";
        }
        else{
            word+=chr;
        }
    }
    return all_words;
}


