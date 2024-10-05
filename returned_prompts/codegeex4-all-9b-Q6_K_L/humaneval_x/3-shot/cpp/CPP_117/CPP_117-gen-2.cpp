    vector<string> all_words;
    string current_word="";
    int level=0;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' '){
            if (current_word.length()>0)
                all_words.push_back(current_word);
            current_word="";
        }
        else{
            current_word+=chr;
        }
    }
    if (current_word.length()>0)
        all_words.push_back(current_word);

    vector<string> all_consonants;
    for (i=0;i<all_words.size();i++){
        current_word=all_words[i];
        int count=0;
        for (int j=0;j<current_word.length();j++){
            chr=current_word[j];
            if (chr=='a' || chr=='e' || chr=='i' || chr=='o' || chr=='u')
                continue;
            count+=1;
        }
        if (count==n)
            all_consonants.push_back(current_word);
    }

    return all_consonants;
}

