    vector<string> all_words;
    string current_word;
    int level=0;
    char chr;
    int i;
    int consonant_counter=0;

    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' ')
        {
            if (consonant_counter==n)
                all_words.push_back(current_word);
            consonant_counter=0;
            current_word="";
        }

        if (chr!=' ')
        {
            current_word+=chr;
            if (chr!='a' && chr!='e' && chr!='i' && chr!='o' && chr!='u')
                consonant_counter+=1;
        }
    }
    return all_words;
}

