    vector<int> pile;
    pile.push_back(n);
    int level = 1;
    while(n > 0){
        if(n % 2 == 0){
            n = n / 2;
        }else{
            n = (n - 1) / 2;
        }
        pile.push_back(n);
        level++;
    }
    return pile;
}

