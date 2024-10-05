    vector<string> words;
    string word;
    if (txt.find(' ') != string::npos) {
        replace(txt.begin(), txt.end(), ' ', '_');
        for (char c : txt) {
            if (c != '_')
                word += c;
            else {
                words.push_back(word);
                word = "";
            }
        }
        words.push_back(word);
    }
    else if (txt.find(',') != string::npos) {
        replace(txt.begin(), txt.end(), ',', '_');
        for (char c : txt) {
            if (c != '_')
                word += c;
            else {
                words.push_back(word);
                word = "";
            }
        }
        words.push_back(word);
    }
    else {
        int count = 0;
        for (char c : txt)
            if (islower(c) && (c - 'a') % 2 == 1)
                count++;
        words.push_back(to_string(count));
    }

    return words;
}

