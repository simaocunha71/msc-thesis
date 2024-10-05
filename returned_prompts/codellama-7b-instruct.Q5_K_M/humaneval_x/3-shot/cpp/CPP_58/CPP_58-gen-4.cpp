    vector<int> l3;
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(l3));
    sort(l3.begin(),l3.end());
    return l3;
}



