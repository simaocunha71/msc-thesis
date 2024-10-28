    sort(l.begin(),l.end());
    vector<int> result;
    int i,j;
    result.push_back(l[0]);
    for (i=1;i<l.size();i++)
    {
        if (l[i]!=l[i-1])
        {
            result.push_back(l[i]);
        }
    }
    return result;
}


