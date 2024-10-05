    vector<int> factors;
    int i,j;
    for (i=2;i<=n;i++){
        if (n%i==0){
            factors.push_back(i);
            while (n%i==0){
                n=n/i;
            }
        }
    }
    return factors;
}

