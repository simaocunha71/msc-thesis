    vector<float> even;
    for (int i=0;i<l.size();i++)
    if (i%2==0)
    even.push_back(l[i]);

    sort(even.begin(),even.end());

    for (int i=0;i<l.size();i++)
    if (i%2==0)
    l[i]=even[i/2];

    return l;
}

