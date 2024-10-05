    transform(str.begin(), str.end(), str.begin(), ::toupper);
    vector<char> distinct_chars(str.begin(), str.end());
    return distinct_chars.size();
}


