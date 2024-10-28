    vector<int> all_diffs;
    int i;
    for (i=0;i<game.size();i++)
    {
        int diff=abs(game[i]-guess[i]);
        all_diffs.push_back(diff);
    }
    return all_diffs;
}

