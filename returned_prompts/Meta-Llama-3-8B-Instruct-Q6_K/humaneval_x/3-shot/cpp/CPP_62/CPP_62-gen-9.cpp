    vector<float> result;
    int i;
    result.push_back(0);
    for (i=1;i<xs.size();i++)
    {
        result.push_back(xs[i]*i);
    }
    return result;
}