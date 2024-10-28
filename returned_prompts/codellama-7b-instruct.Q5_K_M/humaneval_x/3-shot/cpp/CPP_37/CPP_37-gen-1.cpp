    vector<float> l_odd;
    vector<float> l_even;
    int i;
    for (i=0;i<l.size();i++)
        if (i%2==0)
            l_even.push_back(l[i]);
        else
            l_odd.push_back(l[i]);
    
    sort(l_even.begin(),l_even.end());
    vector<float> l_sorted(l_even.size()+l_odd.size());
    int j=0;
    for (i=0;i<l_odd.size();i++)
        l_sorted[j++]=l_odd[i];
    for (i=0;i<l_even.size();i++)
        l_sorted[j++]=l_even[i];
    return l_sorted;
}


