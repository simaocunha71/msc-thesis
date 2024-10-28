    int i;
    vector<float> result;
    result.push_back(xs[1]);
    for (i=1;i<xs.size();i++)
    {
        result.push_back(result[i-1]+(i+1)*xs[i+1]);
    }
    return result;
}



