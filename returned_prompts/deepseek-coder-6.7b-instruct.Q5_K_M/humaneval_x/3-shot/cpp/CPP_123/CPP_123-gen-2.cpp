    vector<int> collatz;
    while(n != 1){
        if(n % 2 != 0)
            collatz.push_back(n);
        n = n % 2 ? n*3 + 1 : n/2;
    }
    collatz.push_back(1);
    sort(collatz.begin(), collatz.end());
    return collatz;
}


