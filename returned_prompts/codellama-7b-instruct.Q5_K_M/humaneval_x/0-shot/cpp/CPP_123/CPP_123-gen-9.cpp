    vector<int> res;
    while(n>1) {
        if(n%2) res.push_back(n);
        if(n%2) n = 3*n + 1;
        else n >>= 1;
    }
    return res;






























