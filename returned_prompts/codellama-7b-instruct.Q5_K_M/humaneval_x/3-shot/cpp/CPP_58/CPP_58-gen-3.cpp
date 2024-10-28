    vector<int> result;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    vector<int>::iterator it;
    it=set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(result));
    return result;
}


