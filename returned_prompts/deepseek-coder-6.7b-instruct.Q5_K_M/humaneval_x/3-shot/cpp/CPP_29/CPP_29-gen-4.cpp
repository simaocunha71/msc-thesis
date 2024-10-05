    vector<string> filtered;
    for  (const auto &str : strings)
        if  (str.substr(0, prefix.size()) == prefix)
            filtered.push_back(str);
    return filtered;
}


