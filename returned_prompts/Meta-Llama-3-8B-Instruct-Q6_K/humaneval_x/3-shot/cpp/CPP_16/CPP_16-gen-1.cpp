    transform(str.begin(), str.end(), str.begin(), ::tolower);
    vector<char> char_set;
    for (char c : str)
        if (find(char_set.begin(), char_set.end(), c) == char_set.end())
            char_set.push_back(c);
    return char_set.size();
}  // end of function


