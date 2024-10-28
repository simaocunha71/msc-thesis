    vector<int> third;
    vector<int> others;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%3==0)
        third.push_back(l[i]);
        else
        others.push_back(l[i]);
    }
    sort(third.begin(),third.end());
    for (i=0;i<third.size();i++)
    {
        l[i*3]=third[i];
    }

    return l;
}

