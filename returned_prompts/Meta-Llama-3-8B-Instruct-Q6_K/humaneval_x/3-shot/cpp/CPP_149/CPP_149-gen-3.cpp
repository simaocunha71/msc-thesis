    vector<string> result;
    for (auto str : lst)
        if (str.length() % 2 == 0)
            result.push_back(str);
    sort(result.begin(), result.end(), [](const string& a, const string& b) {
        if (a.length() == b.length())
            return a < b;
        return a.length() < b.length();
    });
    return result;
} 
