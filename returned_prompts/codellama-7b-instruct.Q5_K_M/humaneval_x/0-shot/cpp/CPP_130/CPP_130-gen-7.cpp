    vector<int> res;
    for(int i=1;i<=n+1;i++){
        if(i%2==0) res.push_back(1+i/2);
        else res.push_back(res[i-1]+res[i-2]+res[i+1]);
    }
    return res;
}

// 2nd round
vector<int> tri(int n) {
    vector<int> res;
    res.push_back(1);
    res.push_back(3);
    res.push_back(2);
    for (int i = 4; i <= n + 1; i++) {
        res.push_back(res[i - 1] + res[i - 2] + res[i + 1]);
    }
    return res;
}
