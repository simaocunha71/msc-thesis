    vector<float> l_even;
    int i,j;
    for (i=0;i<l.size();i++)
    {
        if (i%2==0)
        l_even.push_back(l[i]);
        else
        l_even.push_back(l[i]);
    }
    sort(l_even.begin(),l_even.end());
    return l_even;
}



