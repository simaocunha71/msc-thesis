    vector<int> l_sorted=l;
    sort(l_sorted.begin(), l_sorted.end());
    for (int i=0;i<l.size();i+=3)
    if (i<l.size()-1)
    l[i]=l_sorted[i];
    return l;
}


