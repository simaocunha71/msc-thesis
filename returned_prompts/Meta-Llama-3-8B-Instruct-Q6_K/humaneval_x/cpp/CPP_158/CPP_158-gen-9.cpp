    int max_count = 0, max_word = "";
    for (const auto &word : words) {
        int count = 0;
        set<char> s;
        for (char c : word) {
            if (s.find(c) == s.end()) {
                s.insert(c);
                count++;
            }
        }
        if (count > max_count || (count == max_count && word < max_word)) {
            max_count = count;
            max_word = word;
        }
    }
    return max_word;
}

B:
    int max_count = 0, max_word = "";
    for (const auto &word : words) {
        int count = 0;
        set<char> s;
        for (char c : word) {
            if (s.find(c) == s.end()) {
                s.insert(c);
                count++;
            }
        }
        if (count > max_count) {
            max_count = count;
            max_word = word;
        } else if (count == max_count) {
            if (word < max_word) {
                max_word = word;
            }
        }
    }
    return max_word;
}

int main() {
    vector<string> words = {"name", "of", "string"};
    cout << find_max(words) << endl; // Should print: "string"
    words = {"name", "enam", "game"};
    cout << find_max(words) << endl; // Should print: "enam"
    words = {"aaaaaaa", "bb", "cc"};
    cout << find_max(words) << endl; // Should print: "aaaaaaa"
    return 0;
}

C:
    int max_count = 0, max_word = "";
    for (const auto &word : words) {
        int count = 0;
        set<char> s;
        for (char c : word) {
            if (s.find(c) == s.end()) {
                s.insert(c);
                count++;
            }
        }
        if (count > max_count) {
            max_count = count;
            max_word = word;
        }
    }
    return max_word;
}

D:
    int max_count = 0, max_word = "";
    for (const auto &word : words) {
        int count = 0;
        set<char> s;
        for (char c : word) {
            if (s.find(c) == s.end()) {
                s.insert(c);
               