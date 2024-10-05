    vector<int> result;
    int i;
    for(i=0;i<game.size();i++)
    {
        result.push_back(abs(game[i]-guess[i]));
    }
    return result;
}


