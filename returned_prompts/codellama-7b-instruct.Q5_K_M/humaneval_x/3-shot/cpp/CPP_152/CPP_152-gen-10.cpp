    vector<int> diffs;
    for (int i=0;i<game.size();i++)
    {
        if (game[i]==guess[i])
        diffs.push_back(0);
        else
        diffs.push_back(abs(game[i]-guess[i]));
    }
    return diffs;
}


