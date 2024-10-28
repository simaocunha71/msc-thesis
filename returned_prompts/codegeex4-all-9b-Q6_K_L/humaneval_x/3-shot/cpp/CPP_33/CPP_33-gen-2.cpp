    vector<int> l2;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%3==0)
        l2.push_back(l[i]);
    }
    sort(l2.begin(),l2.end());
    int j=0;
    for (i=0;i<l.size();i++)
    {
        if (i%3==0)
        l[i]=l2[j];
        j+=1;
    }
    return l;
}

