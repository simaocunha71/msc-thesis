    map<char,int> result;
    int max_count = 0;
    for (int i = 0; i < test.length(); i++) {
        char c = test[i];
        if (result.find(c) == result.end()) {
            result[c] = 1;
        } else {
            result[c]++;
        }
        if (result[c] > max_count) {
            max_count = result[c];
        }
    }
    map<char,int> max_result;
    for (auto& p : result) {
        if (p.second == max_count) {
            max_result[p.first] = p.second;
        }
    }
    return max_result;
} // end of function histogram


