    stringstream ss(s);
    vector<string> words;
    string word;
    while (ss >> word)
    words.push_back(word);
    sort(words.begin(), words.end());
    string result;
    for (int i=0;i<words.size();i++)
    result += words[i];
    return result;
}


