    vector<string> all_words;
    int i;
    string current_word;
    bool comma=false;
    bool space=false;
    for (i=0;i<txt.length();i++)
    {
        if (txt[i]==' '){
            if (comma==false){
                all_words.push_back(current_word);
                current_word="";
                space=true;
            }
            else
                current_word+=txt[i];
        }
        if (txt[i]==','){
            if (space==false){
                all_words.push_back(current_word);
                current_word="";
                comma=true;
            }
            else
                current_word+=txt[i];
        }
        if (txt[i]!=' ' && txt[i]!=',')
            current_word+=txt[i];
    }
    if (space==false && comma==false){
        int count=0;
        for (i=0;i<current_word.length();i++)
            if (int(current_word[i])%2==1)
                count+=1;
        all_words.push_back(to_string(count));
    }
    else
        all_words.push_back(current_word);
    return all_words;
}

