    vector<int> pile_levels;
    while (n>0){
        pile_levels.push_back(n);
        if (n%2==0)
        n=n/2;
        else
        n=n/2+1;
    }
    return pile_levels;
}


