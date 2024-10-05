    vector<float> der_xs(xs.size()-1);
    int i;
    for (i=1;i<xs.size();i++)
    der_xs[i-1]=i*xs[i];
    return der_xs;
}



