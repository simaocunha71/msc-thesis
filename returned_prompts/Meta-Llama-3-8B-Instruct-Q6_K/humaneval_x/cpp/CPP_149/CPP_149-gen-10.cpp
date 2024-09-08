    vector<string> res;
    for (string s : lst) {
        if (s.length() % 2 == 0) {
            res.push_back(s);
        }
    }
    sort(res.begin(), res.end(), [](string a, string b) {
        if (a.length() == b.length()) {
            return a < b;
        }
        return a.length() < b.length();
    });
    return res;
}

B:
    vector<string> res;
    for (string s : lst) {
        if (s.length() % 2 == 0) {
            res.push_back(s);
        }
    }
    sort(res.begin(), res.end());
    return res;
}

C:
    vector<string> res;
    for (string s : lst) {
        if (s.length() % 2 == 0) {
            res.push_back(s);
        }
    }
    sort(res.begin(), res.end(), [](string a, string b) {
        if (a.length() == b.length()) {
            return a < b;
        }
        return a.length() < b.length();
    });
    return res;
}

D:
    vector<string> res;
    for (string s : lst) {
        if (s.length() % 2 == 0) {
            res.push_back(s);
        }
    }
    sort(res.begin(), res.end());
    sort(res.begin(), res.end(), [](string a, string b) {
        if (a.length() == b.length()) {
            return a < b;
        }
        return a.length() < b.length();
    });
    return res;
}

E:
    vector<string> res;
    for (string s : lst) {
        if (s.length() % 2 == 0) {
            res.push_back(s);
        }
    }
    sort(res.begin(), res.end(), [](string a, string b) {
        return a.length() < b.length();
    });
    return res;
}

F:
    vector<string> res;
    for (string s : lst) {
        if (s.length() % 2 == 0) {
            res.push_back(s);
        }
    }
    sort(res.begin(), res.end());
    return res;
}

G:
    vector<string> res;
    for (string s : lst) {
        if (s.length() % 2 == 0) {
            res.push_back(s);
        }
    }
    sort(res.begin(), res.end(),