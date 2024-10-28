    vector<int> res;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    set_intersection(l1.begin(), l1.end(), l2.begin(), l2.end(),back_inserter(res));
    res.erase(unique(res.begin(), res.end()), res.end());
    return res;
}


