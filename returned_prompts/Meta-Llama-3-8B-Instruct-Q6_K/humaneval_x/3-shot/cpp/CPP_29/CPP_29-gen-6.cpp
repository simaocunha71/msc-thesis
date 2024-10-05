    vector<string> filtered;
    for (auto &s : strings)
    if (s.find(prefix)==0)
        filtered.push_back(s);
    return filtered;
}