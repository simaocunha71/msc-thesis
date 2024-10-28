    vector<float> even;
    vector<float> odd;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%2==0)
        even.push_back(l[i]);
        else
        odd.push_back(l[i]);
    }
    sort(even.begin(),even.end());
    for (i=0;i<even.size();i++)
    {
        l[i*2]=even[i];
    }
    return l;
}

