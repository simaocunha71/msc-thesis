    vector<int>::iterator it;
    if (lst.size()<2)
    return -1;
    sort(lst.begin(),lst.end());
    it=lower_bound(lst.begin(),lst.end(),lst[0]);
    return *(it);
}


