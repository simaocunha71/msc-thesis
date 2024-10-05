    vector<float> derivative_coeffs;
    int i;
    for  (i=1;i<xs.size();i++)
    {
        derivative_coeffs.push_back(xs[i]*i);
    }
    return derivative_coeffs;
}


