    vector<int> result;
    set<int> s1(l1.begin(),l1.end());
    set<int> s2(l2.begin(),l2.end());
    set<int> intersection;
    set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),std::inserter(intersection,intersection.begin()));
    for (auto x : intersection)
        result.push_back(x);
    sort(result.begin(),result.end());
    return result;
} // This will return a sorted unique common elements in the order they appear in the first list
