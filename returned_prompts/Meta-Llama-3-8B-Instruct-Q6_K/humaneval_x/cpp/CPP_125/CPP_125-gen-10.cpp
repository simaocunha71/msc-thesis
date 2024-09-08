    vector<string> words;
    for(int i=0; i<txt.size(); i++){
        if(txt[i] == ' '){
            words.push_back(txt.substr(0, i));
            txt = txt.substr(i+1);
            i = -1;
        }
    }
    if(txt.size() > 0){
        words.push_back(txt);
    }
    else{
        int count = 0;
        for(int i=0; i<26; i++){
            if(count % 2 == 1 && 'a' + i <= 'z'){
                count++;
            }
        }
        words.push_back(to_string(count));
    }
    return words;
}
B:
    vector<string> split_words(string txt){
    string word;
    vector<string> words;
    for(int i=0; i<txt.size(); i++){
        if(txt[i] == ' ' || txt[i] == ','){
            if(word.size() > 0){
                words.push_back(word);
                word = "";
            }
        }
        else{
            word += txt[i];
        }
    }
    if(word.size() > 0){
        words.push_back(word);
    }
    else{
        int count = 0;
        for(int i=0; i<26; i++){
            if(count % 2 == 1 && 'a' + i <= 'z'){
                count++;
            }
        }
        words.push_back(to_string(count));
    }
    return words;
}
C:
    vector<string> split_words(string txt){
    vector<string> words;
    string word;
    for(int i=0; i<txt.size(); i++){
        if(txt[i] == ' ' || txt[i] == ','){
            if(word.size() > 0){
                words.push_back(word);
                word = "";
            }
            if(txt[i] != ' '){
                words.push_back(to_string(txt[i]));
            }
        }
        else{
            word += txt[i];
        }
    }
    if(word.size() > 0){
        words.push_back(word);
    }
    else{
        int count = 0;
        for(int i=0; i<26; i++){
            if(count % 2 == 1 && 'a' + i <= 'z'){
                count++;
            }
        }
        words.push_back(to_string(count));
    }
    return words;
}D:
    vector<string> split_words(string txt){
    string word;
    vector<string