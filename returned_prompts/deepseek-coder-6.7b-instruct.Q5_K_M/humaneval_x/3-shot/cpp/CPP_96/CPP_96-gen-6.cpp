    vector<int> prime;
    int i, j, isPrime;

    for(i = 2; i <= n; ++i){
        isPrime = 0;

        for(j = 2; j <= i/2; ++j){
            if(i % j == 0){
                isPrime = 1;
                break;
            }
        }

        if(isPrime == 0)
            prime.push_back(i);
    }

    return prime;
}

