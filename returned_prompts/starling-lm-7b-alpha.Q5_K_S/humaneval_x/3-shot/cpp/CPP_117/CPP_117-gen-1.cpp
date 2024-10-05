    vector<string> all_words;
    vector<string> selected_words;
    char chr;
    int i,j;
    string current_word="";
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' ' || chr=='\0')
        {
        if (current_word.length()>0){
            all_words.push_back(current_word);
            current_word="";
        }
        continue;
        }
        if (isalpha(chr)){
        current_word+=chr;
        if (current_word.length()==n){
            selected_words.push_back(current_word);
            current_word="";
        }
        }
    }
    return selected_words;
}


