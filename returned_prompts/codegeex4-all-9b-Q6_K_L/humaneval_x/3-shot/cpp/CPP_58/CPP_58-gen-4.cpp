    vector<int> l3;
    l3= l1;
    l3.insert(l3.end(), l2.begin(), l2.end());
    sort(l3.begin(),l3.end());
    l3.erase(unique(l3.begin(),l3.end()),l3.end());
    return l3;
}

