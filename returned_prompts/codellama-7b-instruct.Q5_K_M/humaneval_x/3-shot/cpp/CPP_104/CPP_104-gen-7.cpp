    vector<int> y;
    for (int i=0;i<x.size();i++)
    {
        if (x[i]%2!=0)
        y.push_back(x[i]);
    }
    sort(y.begin(),y.end());
    return y;
}


