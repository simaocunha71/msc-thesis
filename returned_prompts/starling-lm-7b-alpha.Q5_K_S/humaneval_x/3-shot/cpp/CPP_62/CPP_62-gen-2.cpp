    int i;
    vector<float> derivatives;
    derivatives.push_back(0);
    for (i=1;i<xs.size();i++)
    {
        derivatives.push_back(xs[i-1]*i);
    }
    return derivatives;
}



