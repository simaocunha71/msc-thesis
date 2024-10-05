    vector<int> pile;
    int level=1;
    int stones=n;
    while(stones>0)
    {
        pile.push_back(stones);
        stones+=2;
    }
    return pile;
}

