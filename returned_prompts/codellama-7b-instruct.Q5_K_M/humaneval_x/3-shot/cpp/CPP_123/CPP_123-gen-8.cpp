    vector<int> collatz;
    int i=n;
    while(i>1){
        if (i%2==0)
            i/=2;
        else
            i=3*i+1;
        collatz.push_back(i);
    }
    sort(collatz.begin(),collatz.end());
    return collatz;
}


