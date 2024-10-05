    vector<float> l_even;
    vector<float> l_odd;
    vector<float> l_sorted_even;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%2==0)
        l_even.push_back(l[i]);
        if (i%2==1)
        l_odd.push_back(l[i]);
    }
    l_sorted_even=l_even;
    sort(l_sorted_even.begin(),l_sorted_even.end());
    for (i=0;i<l_odd.size();i++)
    l_sorted_even.push_back(l_odd[i]);
    return l_sorted_even;
}


