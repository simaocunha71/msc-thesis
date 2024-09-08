    int n = xs.size();
    vector<float> result;
    result.push_back(0.0);
    for(int i = 1; i < n; i++){
        result.push_back(xs[i] * i);
    }
    return result;
}

