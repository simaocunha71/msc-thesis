    vector<int> trib;
    if (n <= 1) {
        trib.push_back(3);
        return trib;
    }
    trib.push_back(3);
    trib.push_back(1);
    for (int i = 2; i <= n; i++) {
        int val = 0;
        if (i % 2 == 0) {
            val = 1 + i / 2;
        } else {
            val = trib[i-1] + trib[i-2] + trib[i-3];
        }
        trib.push_back(val);
    }
    return trib;
}