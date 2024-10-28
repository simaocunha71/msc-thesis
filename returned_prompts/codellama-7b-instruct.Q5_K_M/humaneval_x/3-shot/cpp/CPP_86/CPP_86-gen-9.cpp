    stringstream ss(s);
    string current;
    vector<string> words;
    while (getline(ss, current, ' '))
    words.push_back(current);
    sort(words.begin(), words.end());
    string result;
    for (string word : words)
    result += word + ' ';
    return result;
}


