    vector<int> l_sorted(l);
    sort(l_sorted.begin(), l_sorted.end());
    vector<int> l_sorted_third;
    for (int i=0;i<l.size();i++)
    if (i%3==0)
    l_sorted_third.push_back(l_sorted[i]);
    else
    l_sorted_third.push_back(l[i]);
    return l_sorted_third;
}


