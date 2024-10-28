    vector<float> derivatives;
    for (int i=1;i<xs.size();i++)
    derivatives.push_back(xs[i]*i);
    return derivatives;
}



