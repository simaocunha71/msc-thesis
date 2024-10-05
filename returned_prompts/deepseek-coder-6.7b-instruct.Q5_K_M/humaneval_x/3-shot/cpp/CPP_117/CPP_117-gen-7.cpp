    vector<string> words;
    vector<string> selected_words;
    string word = "";
    for (char c : s) {
        if (c == ' ') {
            words.push_back(word);
            word = "";
        } else {
            word += c;
        }
    }
    words.push_back(word);
    for (string w : words) {
        int count = 0;
        for (char c : w) {
            char lower = tolower(c);
            if (lower != 'a' && lower != 'e' && lower != 'i' && lower != 'o' && lower != 'u') {
                count++;
            }
        }
        if (count == n) {
            selected_words.push_back(w);
        }
    }
    return selected_words;
}


