    vector<float> derivative_coefs;
    for(int i=1;i<xs.size();i++){
        derivative_coefs.push_back(xs[i]*i);
    }
    return derivative_coefs;
}

