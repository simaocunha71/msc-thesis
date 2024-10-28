    vector<string> words;
    char chr;
    bool found_space=false;
    string current_word="";
    int i;
    for (i=0;i<txt.length();i++)
    {
        chr=txt[i];
        if (chr==' '){
            found_space=true;
            words.push_back(current_word);
            current_word="";
        }
        else if (found_space==false){
            current_word+=chr;
        }
    }
    words.push_back(current_word);
    return words;
}



