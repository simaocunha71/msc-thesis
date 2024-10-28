    string word = "";
    for (char &c : s) {
        if (c != ' ')
            word += c;
    }
    sort(word.begin(), word.end());
    int idx = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == ' ')
            continue;
        s[i] = word[idx++];
    }
    return s;
}


