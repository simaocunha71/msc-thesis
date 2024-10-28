    vector<float> l_even;
    vector<float> l_odd;
    for (int i=0;i<l.size();i++)
    {
        if (i%2==0)
        l_even.push_back(l[i]);
        else
        l_odd.push_back(l[i]);
    }
    sort(l_even.begin(), l_even.end());
    vector<float> l_sorted;
    for (int i=0;i<l_even.size();i++)
    {
        l_sorted.push_back(l_even[i]);
        l_sorted.push_back(l_odd[i]);
    }
    return l_sorted;
}


