    vector<string> words;
    string word;
    for (char c : s) {
        if (c == ',' || c == ' ') {
            words.push_back(word);
            word = "";
        } else {
            word += c;
        }
    }
    words.push_back(word);
    return words;
}