    vector<int> result(n);
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            result[i-1] = 1;
            for (int j = 2; j <= i; j++) {
                result[i-1] *= j;
            }
        } else {
            result[i-1] = 0;
            for (int j = 1; j <= i; j++) {
                result[i-1] += j;
            }
        }
    }
    return result;
}


