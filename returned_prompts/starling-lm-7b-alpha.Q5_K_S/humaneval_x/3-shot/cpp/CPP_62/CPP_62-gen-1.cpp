    vector<float> deriv;
    int i;
    for (i=0;i<xs.size()-1;i++)
    {
        deriv.push_back(i*xs[i]);
    }
    deriv.push_back(xs[i]);
    return deriv;
}


