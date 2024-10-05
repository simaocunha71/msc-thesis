    vector<string> words;
    vector<string> result;
    string word = "";
    for (int i = 0; i < s.length(); i++){
        if (s[i] == ' '){
            words.push_back(word);
            word = "";
        } else {
            word += s[i];
        }
    }
    words.push_back(word);
    for (string w : words){
        int consonants = 0;
        for (char c : w){
            if (tolower(c) >= 'a' && tolower(c) <= 'z'){
                char lc = tolower(c);
                if (lc != 'a' && lc != 'e' && lc != 'i' && lc != 'o' && lc != 'u'){
                    consonants++;
                }
            }
        }
        if (consonants == n){
            result.push_back(w);
        }
    }
    return result;
}

