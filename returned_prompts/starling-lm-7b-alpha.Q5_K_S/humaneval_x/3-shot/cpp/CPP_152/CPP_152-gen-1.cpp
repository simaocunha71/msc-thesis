    int i,length=game.size();
    vector<int> result;
    for (i=0;i<length;i++)
    result.push_back(abs(game[i]-guess[i]));
    return result;
}


