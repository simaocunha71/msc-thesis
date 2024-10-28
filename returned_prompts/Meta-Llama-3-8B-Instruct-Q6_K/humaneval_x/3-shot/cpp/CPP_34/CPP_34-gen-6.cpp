    vector<int> unique_vector;
    set<int> s(l.begin(), l.end());
    for (auto i : s) {
        unique_vector.push_back(i);
    }
    return unique_vector;
} 

