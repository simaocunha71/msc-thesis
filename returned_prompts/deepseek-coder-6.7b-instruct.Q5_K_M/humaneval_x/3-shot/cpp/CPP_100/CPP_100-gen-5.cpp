    vector<int> pile;
    for(int i = 0; i < n; i++){
        if(n % 2 == 0)
            pile.push_back(n + (2 * i));
        else
            pile.push_back(n + (2 * i));
    }
    return pile;
}


