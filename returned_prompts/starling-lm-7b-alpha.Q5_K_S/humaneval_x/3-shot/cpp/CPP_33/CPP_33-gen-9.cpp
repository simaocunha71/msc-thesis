    vector<int> third;
    int i;
    for (i=0;i<l.size();i++)
    if (i%3==0)
    third.push_back(i);

    sort(third.begin(),third.end());

    vector<int> l_;
    for (i=0;i<l.size();i++)
    if (i%3!=0)
    l_.push_back(l[i]);
    for (i=0;i<third.size();i++)
    l_.push_back(l[third[i]]);

    return l_;
}



