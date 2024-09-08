    vector<int> result;
    int max_level = 0;
    for (string group : split(paren_string, " ")) {
        int level = 0;
        for (char c : group) {
            if (c == '(') {
                level++;
            } else if (c == ')') {
                level--;
            }
            max_level = max(max_level, level);
        }
        result.push_back(max_level);
        max_level = 0;
    }
    return result;
}

