    vector<string> result;
    for (auto str : lst) {
        if (str.size() % 2 == 0) {
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end());
    return result;
}


