    vector<int> factors;
    for(int i = 2; n != 1; i++) {
        while(n % i == 0) {
            factors.push_back(i);
            n = n / i;
        }
    }
    return factors;
}


