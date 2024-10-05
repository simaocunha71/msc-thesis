    vector<string> words;
    string word = "";
    int count = 0;
    for (int i = 0; i < txt.length(); i++){
        if (txt[i] == ' ' || txt[i] == ','){
            if (word != ""){
                words.push_back(word);
                word = "";
            }
        }
        else {
            if (islower(txt[i])){
                if ((txt[i] - 'a') % 2 == 1){
                    count++;
                }
            }
            else {
                word += txt[i];
            }
        }
    }
    if (word != ""){
        words.push_back(word);
    }
    if (count == 0){
        words.clear();
        words.push_back(to_string(count));
    }
    else {
        words.push_back(to_string(count));
    }
    return words;
}

