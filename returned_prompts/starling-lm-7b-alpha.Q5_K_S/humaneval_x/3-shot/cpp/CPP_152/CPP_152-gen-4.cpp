    vector<int> diff;
    int i,a,b;
    for (i=0;i<game.size();i++)
    {
        a=game[i];
        b=guess[i];
        diff.push_back(abs(a-b));
    }
    return diff;
}


