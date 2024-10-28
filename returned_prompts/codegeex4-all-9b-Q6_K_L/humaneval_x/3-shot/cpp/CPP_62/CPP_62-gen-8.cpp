    vector<float> xs_der;
    int i;
    for (i=0;i<xs.size()-1;i++)
    xs_der.push_back(xs[i+1]*(i+1));
    return xs_der;
}

