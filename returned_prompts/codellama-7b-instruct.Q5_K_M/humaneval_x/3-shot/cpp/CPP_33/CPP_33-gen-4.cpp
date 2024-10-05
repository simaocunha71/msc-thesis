    vector<int> l_odd, l_even;
    for (int i=0;i<l.size();i++)
    if (i%3!=0)
    l_odd.push_back(l[i]);
    else
    l_even.push_back(l[i]);
    sort(l_even.begin(), l_even.end());
    vector<int> l_sorted;
    for (int i=0;i<l.size();i++)
    if (i%3!=0)
    l_sorted.push_back(l_odd[i]);
    else
    l_sorted.push_back(l_even[i%3]);
    return l_sorted;
}

