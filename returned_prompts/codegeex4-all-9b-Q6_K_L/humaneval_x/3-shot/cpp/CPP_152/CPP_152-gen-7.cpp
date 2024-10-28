    vector<int> result;
    int i,j;
    for (i=0;i<game.size();i++)
    {
        j=game[i]-guess[i];
        if (j>0)
        result.push_back(j);
        else
        result.push_back(-j);
    }
    return result;
}