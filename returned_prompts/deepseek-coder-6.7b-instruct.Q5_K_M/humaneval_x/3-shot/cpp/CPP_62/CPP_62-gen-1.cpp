    int i;
    for (i=0;i<xs.size()-1;i++)
    xs[i]=xs[i]*(xs.size()-1-i);
    xs.pop_back();
    return xs;
}


