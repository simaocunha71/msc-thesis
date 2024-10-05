    int i;
    vector<float> result;
    result.push_back(0);
    for (i=1;i<xs.size();i++)
    {
        result.push_back(xs[i-1]*i);
    }
    return result;
}



