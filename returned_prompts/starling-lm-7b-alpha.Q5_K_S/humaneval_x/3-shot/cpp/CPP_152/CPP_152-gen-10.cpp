    vector<int> diff;
    int i;
    int g;
    int s;
    int diff_i;
    for (i=0;i<game.size();i++)
    {
        g=guess[i];
        s=game[i];
        diff_i=abs(g-s);
        diff.push_back(diff_i);
    }
    return diff;
}



