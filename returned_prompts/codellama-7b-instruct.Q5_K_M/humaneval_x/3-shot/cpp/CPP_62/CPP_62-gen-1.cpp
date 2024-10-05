    vector<float> deriv;
    int i;
    for (i=1;i<xs.size();i++)
    deriv.push_back(xs[i]*float(i));
    return deriv;
}


