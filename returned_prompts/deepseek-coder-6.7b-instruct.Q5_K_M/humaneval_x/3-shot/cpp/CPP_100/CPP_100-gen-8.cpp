    vector<int> pile;
    int next_stone = n;
    for (int i=0; i<n; i++){
        pile.push_back(next_stone);
        if (next_stone % 2 == 0) {
            next_stone += 2;
        } else {
            next_stone += 2;
        }
    }
    return pile;
}



