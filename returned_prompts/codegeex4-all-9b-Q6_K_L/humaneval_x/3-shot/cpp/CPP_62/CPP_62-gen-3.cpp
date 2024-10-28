    vector<float> new_xs;
    int i;
    for (i=0;i<xs.size()-1;i++)
    new_xs.push_back(xs[i+1]*(i+1));
    return new_xs;
}

