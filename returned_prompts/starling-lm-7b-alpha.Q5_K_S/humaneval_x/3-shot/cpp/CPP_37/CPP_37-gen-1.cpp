    int i;
    vector<float> l_even;
    for (i=0;i<l.size();i++)
    if (i%2==0)
    {
        l_even.push_back(l[i]);
    }
    sort(l_even.begin(),l_even.end());
    for (i=0;i<l_even.size();i++)
    {
        l[i]=l_even[i];
    }
    return l;
}

