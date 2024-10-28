    vector<int> res;
    for (int i = 0; i < n; i++){
        res.push_back(n);
        n = (n % 2 == 0) ? n + 1 : n + 2;
    }
    return res;
}

