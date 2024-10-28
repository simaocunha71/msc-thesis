    vector<int> third;
    int i;
    for (i=0;i<l.size();i++)
    if (i%3==0)
    third.push_back(l[i]);

    sort(third.begin(),third.end());

    for (i=0;i<l.size();i++)
    if (i%3==0)
    l[i]=third[i/3];

    return l;
}


