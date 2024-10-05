    vector<float> result;
    result.push_back(0);
    for (int i=1;i<xs.size();i++)
    {
        result.push_back(xs[i]*i);
    }
    return result;
}  // 1st order derivative


