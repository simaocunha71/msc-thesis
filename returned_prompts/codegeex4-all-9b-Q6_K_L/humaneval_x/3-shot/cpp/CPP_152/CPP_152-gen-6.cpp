    int i;
    vector<int> game1;
    for (i=0;i<game.size();i++)
    game1.push_back(abs(game[i]-guess[i]));
    return game1;
}

