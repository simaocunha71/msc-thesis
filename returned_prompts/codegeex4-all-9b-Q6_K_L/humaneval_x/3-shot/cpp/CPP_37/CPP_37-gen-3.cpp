    vector<float> even_indicies;
    int i;
    for (i=0;i<l.size();i+=2)
    even_indicies.push_back(l[i]);
    sort(even_indicies.begin(),even_indicies.end());
    for (i=0;i<l.size();i+=2)
    l[i]=even_indicies[i/2];
    return l;
}

