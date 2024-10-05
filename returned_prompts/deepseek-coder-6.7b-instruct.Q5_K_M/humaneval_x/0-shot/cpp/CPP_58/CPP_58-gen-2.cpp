    sort(l1.begin(), l1.end());
    sort(l2.begin(), l2.end());
    vector<int> v;
    set_intersection(l1.begin(), l1.end(), l2.begin(), l2.end(), back_inserter(v));
    v.erase(unique(v.begin(), v.end()), v.end());
    return v;
}

*/

