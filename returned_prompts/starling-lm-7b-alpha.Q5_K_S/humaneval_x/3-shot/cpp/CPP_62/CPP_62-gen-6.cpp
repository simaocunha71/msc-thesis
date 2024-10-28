    vector<float> derivatives;
    derivatives.resize(xs.size());
    derivatives[0]=0;
    int i;
    for (i=1;i<xs.size();i++)
    {
        derivatives[i]=i*xs[i-1];
    }
    return derivatives;
}



