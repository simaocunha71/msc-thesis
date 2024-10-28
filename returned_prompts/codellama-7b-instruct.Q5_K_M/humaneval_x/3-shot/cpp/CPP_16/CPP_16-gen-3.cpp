    transform(str.begin(), str.end(), str.begin(), ::tolower);
    vector<char> v(str.begin(), str.end());
    return unique(v.begin(), v.end()) - v.begin();
}


