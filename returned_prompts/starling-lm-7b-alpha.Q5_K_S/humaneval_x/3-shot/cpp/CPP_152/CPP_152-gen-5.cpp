    vector<int> results;
    int i,abs_diff;
    for (i=0;i<game.size();i++)
    {
        abs_diff=abs(game[i]-guess[i]);
        results.push_back(abs_diff);
    }
    return results;
}


