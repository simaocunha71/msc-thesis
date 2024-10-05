    vector<float> l_even, l_odd;
    int i;
    for (i=0;i<l.size();i++)
    if (i%2==0)
    l_even.push_back(l[i]);
    else
    l_odd.push_back(l[i]);
    sort(l_even.begin(), l_even.end());
    for (i=0;i<l_even.size();i++)
    l_odd[i*2]=l_even[i];
    return l_odd;
}


