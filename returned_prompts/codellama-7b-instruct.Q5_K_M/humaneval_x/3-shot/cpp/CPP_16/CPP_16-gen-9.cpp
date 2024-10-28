    transform(str.begin(), str.end(), str.begin(), ::tolower);
    vector<char> char_set(str.begin(), str.end());
    return unique(char_set.begin(), char_set.end()).size();
}


