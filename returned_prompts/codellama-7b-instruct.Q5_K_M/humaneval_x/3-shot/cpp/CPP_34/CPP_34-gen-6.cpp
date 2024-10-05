    sort(l.begin(),l.end());
    vector<int>::iterator last_unique=unique(l.begin(),l.end());
    l.erase(last_unique,l.end());
    return l;
}


