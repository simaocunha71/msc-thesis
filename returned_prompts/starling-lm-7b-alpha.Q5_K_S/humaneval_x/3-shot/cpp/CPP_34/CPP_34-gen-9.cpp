    sort(l.begin(),l.end());
    vector<int> result;
    int prev=-1;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (l[i]!=prev)
        {
            result.push_back(l[i]);
            prev=l[i];
        }
    }
    return result;
}



