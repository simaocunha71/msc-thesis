    vector<int> pile;
    pile.push_back(n);
    int i=1;
    while (n>1){
        n=abs(n-1)%2==0?n+1:n-1;
        pile.push_back(n);
        i++;
    }
    return pile;
}

