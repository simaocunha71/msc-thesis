    vector<int> collatz;
    int i=1;
    while (i<=n){
        collatz.push_back(i);
        i*=2;
    }
    sort(collatz.begin(), collatz.end());
    return collatz;
}

