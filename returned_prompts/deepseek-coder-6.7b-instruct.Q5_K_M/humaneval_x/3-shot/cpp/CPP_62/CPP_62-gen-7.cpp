    int i;
    for(i=1;i<xs.size();i++)
    xs[i]=xs[i]*i;
    xs.erase(xs.begin());
    return xs;
}


