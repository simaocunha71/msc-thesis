    vector<float> l2;
    for (int i=0;i<l.size();i++)
    {
        if (i%2==0)
        {
            l2.push_back(l[i]);
        }
        else
        {
            l2.push_back(l[i]);
        }
    }
    sort(l2.begin(),l2.end());
    return l2;
}
