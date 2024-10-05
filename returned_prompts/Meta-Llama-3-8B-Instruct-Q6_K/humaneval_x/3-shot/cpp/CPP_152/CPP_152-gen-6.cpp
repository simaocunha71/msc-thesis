    vector<int> results;
    int i;
    for (i=0;i<game.size();i++)
    {
        results.push_back(abs(guess[i]-game[i]));
    }
    return results;
}