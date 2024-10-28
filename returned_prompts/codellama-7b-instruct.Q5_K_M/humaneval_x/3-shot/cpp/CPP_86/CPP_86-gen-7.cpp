    stringstream ss(s);
    vector<string> words;
    string word;
    while(ss >> word)
        words.push_back(word);

    sort(words.begin(), words.end(), [](string a, string b) { return a < b; });
    string result;
    for (auto word : words)
    {
        result += word;
        result += " ";
    }
    result.pop_back();
    return result;
}


