    vector<int> primes;
    bool is_prime;
    for (int i = 2; i < n; i++) {
        is_prime = true;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime)
            primes.push_back(i);
    }
    return primes;
}

