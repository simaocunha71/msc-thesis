    for (int i=0;i<xs.size();i++)
    xs[i]=xs[i]*(xs.size()-i-1);
    xs.pop_back();
    return xs;
}


