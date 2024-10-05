    vector<string> words;
    vector<string> result;
    string temp = "";
    for (int i = 0; i < s.length(); i++){
        if (s[i] == ' '){
            words.push_back(temp);
            temp = "";
        }
        else{
            temp += s[i];
        }
    }
    words.push_back(temp);
    for (string word : words){
        int count = 0;
        for (char c : word){
            char lower_c = tolower(c);
            if (lower_c != 'a' && lower_c != 'e' && lower_c != 'i' && lower_c != 'o' && lower_c != 'u' && isalpha(c)){
                count++;
            }
        }
        if (count == n){
            result.push_back(word);
        }
    }
    return result;
}

