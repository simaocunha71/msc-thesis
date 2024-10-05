    vector<float> res;
    res.push_back(0.0);
    for (int i=1;i<xs.size();i++)
    {
        res.push_back(i*xs[i]);
    }
    return res;
}