    vector<int> result;
    set<int> s1(l1.begin(),l1.end());
    set<int> s2(l2.begin(),l2.end());
    set<int> intersection;
    set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),std::inserter(intersection,intersection.begin()));
    for (auto it=intersection.begin();it!=intersection.end();++it)
    {
        result.push_back(*it);
    }
    sort(result.begin(),result.end());
    return result;
}  // This function sorts the vector automatically if you use std::set_intersection with std::set. Otherwise it manually sorts. It uses set to remove duplicates. It also returns a sorted vector.