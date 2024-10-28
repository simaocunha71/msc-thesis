    map<char,int> res;
    if (test.size() == 0) return res;
    int max_count = 0;
    for (char c : test) {
        if (res.find(c) != res.end()) {
            res[c]++;
        } else {
            res[c] = 1;
        }
        if (res[c] > max_count) {
            max_count = res[c];
        }
    }
    for (auto it = res.begin(); it != res.end(); it++) {
        if (it->second == max_count) {
            cout << it->first << " " << it->second << endl;
        }
    }
    return res;
}
