    vector<int> result(game.size());
    for (int i = 0; i < game.size(); i++)
        result[i] = abs(game[i] - guess[i]);
    return result;
}


