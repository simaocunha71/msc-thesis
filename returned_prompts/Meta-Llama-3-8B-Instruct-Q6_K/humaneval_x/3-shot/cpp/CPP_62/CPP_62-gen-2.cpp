    vector<float> result;
    int i;
    for (i=1;i<xs.size();i++)
    {
        result.push_back(i*xs[i]);
    }
    return result;
}

