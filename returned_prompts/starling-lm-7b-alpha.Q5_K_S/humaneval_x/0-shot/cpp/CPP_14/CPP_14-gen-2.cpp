    vector<string> res;
    if(str.length() <= 2) {
        vector<string> tmp;
        for(char c: str) tmp.push_back(string(1,c));
        for(string s: tmp) res.push_back(s);
        return res;
    }
    int n = str.length();
    for(int i = 0; i < n; i++) {
        string tmp = str;
        tmp.erase(i, 1);
        for(string s: all_perms(tmp)) {
            res.push_back(str.substr(0, i) + s + str.substr(i+1));
        }
    }
    return res;
}


/*
Return the lexicographically smallest string that can be formed from the input string
>>> min_string("abc")
