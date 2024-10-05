    vector<float> new_xs;
    for (int i=1;i<xs.size();i++)
    {
        new_xs.push_back(xs[i]*i);
    }
    return new_xs;
}

