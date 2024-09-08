    vector<int> factors;
    int i = 2;
    while (i * i <= n) {
        int count = 0;
        while (n % i == 0) {
            n /= i;
            count++;
        }
        if (count > 0) {
            for (int j = 0; j < count; j++) {
                factors.push_back(i);
            }
        }
        i++;
    }
    if (n > 1) {
        factors.push_back(n);
    }
    return factors;
} 

