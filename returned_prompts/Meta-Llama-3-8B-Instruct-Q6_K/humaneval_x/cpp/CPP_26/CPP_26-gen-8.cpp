    vector<int> result;
    for(int i = 0; i < numbers.size(); i++) {
        bool found = false;
        for(int j = 0; j < result.size(); j++) {
            if(numbers[i] == result[j]) {
                found = true;
                break;
            }
        }
        if(!found) {
            result.push_back(numbers[i]);
        }
    }
    return result;
}

B:
    vector<int> result;
    for(int i = 0; i < numbers.size(); i++) {
        bool found = false;
        for(int j = 0; j < result.size(); j++) {
            if(numbers[i] == result[j]) {
                found = true;
                break;
            }
        }
        if(!found) {
            result.push_back(numbers[i]);
        }
    }
    return result;
}

C:
    set<int> s(numbers.begin(), numbers.end());
    vector<int> result(s.begin(), s.end());
    return result;

D:
    map<int, int> m;
    vector<int> result;
    for(int i = 0; i < numbers.size(); i++) {
        m[numbers[i]]++;
    }
    for(map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
        if(it->second == 1) {
            result.push_back(it->first);
        }
    }
    return result;
}D:
    map<int, int> m;
    vector<int> result;
    for(int i = 0; i < numbers.size(); i++) {
        m[numbers[i]]++;
    }
    for(map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
        if(it->second == 1) {
            result.push_back(it->first);
        }
    }
    return result;
}D:
    map<int, int> m;
    vector<int> result;
    for(int i = 0; i < numbers.size(); i++) {
        m[numbers[i]]++;
    }
    for(map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
        if(it->second == 1) {
            result.push_back(it->first);
        }
    }
    return result;
}

E:
    unordered_map<int, int> m;
    vector<int> result;
    for(int i = 0; i < numbers.size(); i++) {
        m[numbers[i]]