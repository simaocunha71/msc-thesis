    vector<int> l_sorted;
    vector<int> l_third;
    int i,j;
    for (i=0;i<l.size();i++)
    {
        if (i%3==0)
        {
            sort(l.begin(),l.end());
            l_sorted=l;
        }
        if (i%3!=0)
        {
            l_third.push_back(l[i]);
        }
    }
    l_sorted.insert(l_sorted.end(),l_third.begin(),l_third.end());
    return l_sorted;
}






