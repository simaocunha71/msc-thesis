    vector<float> l_even;
    for (int i=0;i<l.size();i+=2)
    l_even.push_back(l[i]);

    sort(l_even.begin(),l_even.end());

    vector<float> l_odd;
    for (int i=1;i<l.size();i+=2)
    l_odd.push_back(l[i]);

    vector<float> l_sorted;
    l_sorted.insert(l_sorted.end(),l_even.begin(),l_even.end());
    l_sorted.insert(l_sorted.end(),l_odd.begin(),l_odd.end());

    return l_sorted;
}


