    vector<int> new_l;
    vector<int> third;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%3==0)
        {
            third.push_back(l[i]);
        }
    }
    sort(third.begin(),third.end());
    for (i=0;i<l.size();i++)
    {
        if (i%3==0)
        {
            new_l.push_back(third[i/3]);
        }
        else
        {
            new_l.push_back(l[i]);
        }
    }
    return new_l;
}

