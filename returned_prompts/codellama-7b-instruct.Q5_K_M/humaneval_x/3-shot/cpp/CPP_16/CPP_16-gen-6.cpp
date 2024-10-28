    vector<char> unique_char;
    transform(str.begin(), str.end(), back_inserter(unique_char), ::tolower);
    return unique_char.size();
}


