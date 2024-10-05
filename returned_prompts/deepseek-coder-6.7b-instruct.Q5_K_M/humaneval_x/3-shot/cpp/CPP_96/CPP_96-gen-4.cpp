    vector<int> primes;
    int i,j,isPrime;
    for(i=2;i<n;i++){
        isPrime = 1;
        for(j=2;j*j<=i;j++){
            if(i%j==0){
                isPrime = 0;
                break;
            }
        }
        if(isPrime==1){
            primes.push_back(i);
        }
    }
    return primes;
}


