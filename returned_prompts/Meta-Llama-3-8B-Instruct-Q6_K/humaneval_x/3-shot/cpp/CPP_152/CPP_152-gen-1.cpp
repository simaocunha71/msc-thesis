    vector<int> result;
    int i;
    for (i=0;i<game.size();i++)
    {
        if (game[i]==guess[i])
            result.push_back(0);
        else
            result.push_back(abs(guess[i]-game[i]));
    }
    return result;
}  