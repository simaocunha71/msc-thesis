    int i;
    vector<float> even;
    for (i=0;i<l.size();i+=2)
    {
        even.push_back(l[i]);
    }

    sort(even.begin(),even.end());

    for (i=0;i<even.size();i++)
    {
        l[i*2]=even[i];
    }

    return l;
}


