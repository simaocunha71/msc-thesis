    vector<float> derivatives;
    int n=xs.size();
    int i;
    for (i=1;i<n;i++)
    derivatives.push_back(i*xs[i]);
    return derivatives;
}


