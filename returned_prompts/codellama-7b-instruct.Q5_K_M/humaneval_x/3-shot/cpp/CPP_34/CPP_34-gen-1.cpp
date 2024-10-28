    sort(l.begin(), l.end());
    vector<int>::iterator it;
    it=unique(l.begin(), l.end());
    l.resize(it-l.begin());
    return l;
}


