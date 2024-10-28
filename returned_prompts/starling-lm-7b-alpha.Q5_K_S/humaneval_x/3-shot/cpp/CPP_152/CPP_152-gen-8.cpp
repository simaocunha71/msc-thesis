    vector<int> results;
    int i;
    for (i=0;i<game.size();i++)
    {
        results.push_back(abs(game[i]-guess[i]));
    }
    return results;
}



