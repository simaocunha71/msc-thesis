    sort(l.begin(),l.end());
    vector<int>::iterator it;
    it = unique(l.begin(),l.end());
    l.resize(distance(l.begin(),it));
    return l;
}

