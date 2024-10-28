    vector<float> l2;
    for(int i=0;i<l.size();i++)
    {
        if(i%2==0)
        {
            l2.push_back(l[i]);
        }
    }
    sort(l2.begin(),l2.end());
    for(int i=0;i<l.size();i++)
    {
        if(i%2==0)
        {
            l[i]=l2[0];
            l2.erase(l2.begin());
        }
    }
    return l;
}
