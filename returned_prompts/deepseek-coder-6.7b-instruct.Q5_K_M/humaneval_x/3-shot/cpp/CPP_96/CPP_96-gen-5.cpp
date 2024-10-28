    vector<int> primes;
    if(n <= 1)
        return primes;
    primes.push_back(2);
    for(int i = 3; i < n; i += 2) {
        bool isPrime = true;
        for(int j = 0; j < primes.size(); j++) {
            if(i % primes[j] == 0) {
                isPrime = false;
                break;
            }
            if(primes[j] * primes[j] > i) {
                break;
            }
        }
        if(isPrime)
            primes.push_back(i);
    }
    return primes;
}


