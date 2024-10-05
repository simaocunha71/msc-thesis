    vector<int> diff;
    int i;
    for (i=0;i<game.size();i++){
        if (game[i]==guess[i])
            diff.push_back(0);
        else
            diff.push_back(abs(guess[i]-game[i]));
    }
    return diff;
}