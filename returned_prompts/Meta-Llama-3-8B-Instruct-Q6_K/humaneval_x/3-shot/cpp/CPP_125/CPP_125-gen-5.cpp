    vector<string> words;
    size_t pos;
    string token;
    if (txt.find(" ") != string::npos) {
        pos = 0;
        while ((pos = txt.find(" ")) != string::npos) {
            token = txt.substr(0, pos);
            words.push_back(token);
            txt.erase(0, pos + 1);
        }
        if (!txt.empty()) {
            words.push_back(txt);
        }
    } else if (txt.find(",") != string::npos) {
        pos = 0;
        while ((pos = txt.find(",")) != string::npos) {
            token = txt.substr(0, pos);
            words.push_back(token);
            txt.erase(0, pos + 1);
        }
        if (!txt.empty()) {
            words.push_back(txt);
        }
    } else {
        int count = 0;
        for (char c : txt) {
            if (c >= 'a' && c <= 'z') {
                count += (c - 'a');
            }
        }
        words.push_back(to_string(count));
    }
    return words;
}
