    int i;
    vector<float> deri;
    for (i=1;i<xs.size();i++)
    {
        deri[i-1]=xs[i]*i;
    }
    return deri;
}

