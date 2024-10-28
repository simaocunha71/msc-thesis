    vector<float> derivative;
    int i;
    for (i=1; i<xs.size(); i++)
    {
        derivative.push_back(xs[i]*i);
    }
    return derivative;
}

