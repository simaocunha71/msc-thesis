    vector<string> words;
    vector<string> results;
    string word = "";
    for (int i = 0; i < s.length(); i++) {
        if (s[i] != ' ')
            word += s[i];
        else {
            words.push_back(word);
            word = "";
        }
    }
    words.push_back(word);
    for (string w : words) {
        int c = 0;
        for (char l : w)
            if (tolower(l) != 'a' && tolower(l) != 'e' && tolower(l) != 'i' && tolower(l) != 'o' && tolower(l) != 'u' && isalpha(l))
                c++;
        if (c == n)
            results.push_back(w);
    }
    return results;
}


