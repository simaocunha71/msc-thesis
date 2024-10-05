    vector<int> result;
    int i;
    for (i=0;i<game.size();i++)
    {
        if (guess[i]==game[i])
        result.push_back(0);
        else
        result.push_back(abs(guess[i]-game[i]));
    }
    return result;
}


