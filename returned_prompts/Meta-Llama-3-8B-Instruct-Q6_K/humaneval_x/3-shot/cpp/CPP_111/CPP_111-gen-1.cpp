    map<char,int> result;
    if (test.empty())
        return result;
    int max_count = 0;
    int max_count_letter = 0;
    for (int i = 0; i < test.size(); i++) {
        if (test[i] != ' ') {
            char c = test[i];
            if (result.find(c) == result.end()) {
                result[c] = 1;
            } else {
                result[c]++;
            }
            if (result[c] > max_count) {
                max_count = result[c];
                max_count_letter = c;
            }
        }
    }
    for (auto it = result.begin(); it != result.end(); it++) {
        if (it->second == max_count) {
            result[it->first] = max_count;
        } else {
            result.erase(it->first);
        }
    }
    return result;
}
