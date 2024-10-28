    int count = 0;
    vector<int> a;
    for(int i = 1; i <= n; i++) {
        a.push_back(i * i - i + 1);
    }
    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            for(int k = j + 1; k < n; k++) {
                if((a[i] + a[j] + a[k]) % 3 == 0) {
                    count++;
                }
            }
        }
    }
    return count;
}  // 0(n^2) time complexity


