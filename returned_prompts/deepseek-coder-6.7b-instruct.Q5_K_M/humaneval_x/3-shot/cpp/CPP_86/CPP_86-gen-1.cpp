    string word = "";
    for (char &c : s) {
        if (c == ' ') {
            sort(word.begin(), word.end());
            s.replace(s.find(word), word.length(), word);
            word = "";
        } else {
            word += c;
        }
    }
    sort(word.begin(), word.end());
    s.replace(s.find(word), word.length(), word);

    return s;
}


