    sort(lst.begin(), lst.end(), [](const string& a, const string& b) {
        return a.length() < b.length() || (a.length() == b.length() && a < b);
    });
    vector<string> result;
    for (int i = 0; i < lst.size(); ++i) {
        if (lst[i].length() % 2 == 0)
            result.push_back(lst[i]);
    }
    return result;
}



