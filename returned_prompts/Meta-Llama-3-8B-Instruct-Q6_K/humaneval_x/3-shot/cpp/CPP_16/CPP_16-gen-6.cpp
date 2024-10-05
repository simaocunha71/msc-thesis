    unordered_set<char> s;
    for (char c : str) {
        c = tolower(c);
        if (c >= 'a' && c <= 'z') {
            s.insert(c);
        }
    }
    return s.size();
}  //