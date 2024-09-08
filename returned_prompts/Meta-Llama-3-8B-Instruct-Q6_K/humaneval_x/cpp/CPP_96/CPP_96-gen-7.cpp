    vector<int> primes;
    if(n<2) return primes; // if n is less than 2, no primes are less than n
    for(int i=2; i<n; i++){
        bool is_prime = true;
        for(int j=2; j*j<=i; j++){
            if(i%j == 0){
                is_prime = false;
                break;
            }
        }
        if(is_prime){
            primes.push_back(i);
        }
    }
    return primes;
}

B:
    vector<int> count_up_to(int n){
        vector<int> primes;
        for(int i=2; i<n; i++){
            if(is_prime(i)){
                primes.push_back(i);
            }
        }
        return primes;
    }

    bool is_prime(int n){
        if(n<2) return false;
        for(int i=2; i*i<=n; i++){
            if(n%i == 0) return false;
        }
        return true;
    }
C:
    vector<int> count_up_to(int n){
        vector<int> primes;
        for(int i=2; i<n; i++){
            if(is_prime(i)){
                primes.push_back(i);
            }
        }
        return primes;
    }

    bool is_prime(int n){
        if(n<2) return false;
        for(int i=2; i*i<=n; i++){
            if(n%i == 0) return false;
        }
        return true;
    }

D:
    vector<int> count_up_to(int n){
        vector<int> primes;
        for(int i=2; i<n; i++){
            if(is_prime(i)){
                primes.push_back(i);
            }
        }
        return primes;
    }

    bool is_prime(int n){
        if(n<2) return false;
        for(int i=2; i*i<=n; i++){
            if(n%i == 0) return false;
        }
        return true;
    }

E:
    vector<int> count_up_to(int n){
        vector<int> primes;
        for(int i=2; i<n; i++){
            if(is_prime(i)){
                primes.push_back(i);
            }
        }
        return primes;
    }

    bool is_prime(int n){
        if(n<2) return false;
        for(int i=2; i*i<=n; i++){
            if(n%i == 0) return false;
        }
        return true;
    }

F:
