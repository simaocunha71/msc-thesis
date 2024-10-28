    vector<int> char_count(256, 0);
    int distinct_chars = 0;
    for (int i=0; i<str.size(); i++) {
        int c = str[i];
        if (char_count[c] == 0) {
            distinct_chars++;
        }
        char_count[c]++;
    }
    return distinct_chars;
}

