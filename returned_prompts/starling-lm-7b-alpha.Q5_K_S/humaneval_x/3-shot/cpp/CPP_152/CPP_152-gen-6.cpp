    int i;
    vector<int> result;
    int a,b;
    for (i=0;i<game.size();i++)
    {
        a=game[i];
        b=guess[i];
        result.push_back(abs(a-b));
    }
    return result;
}


