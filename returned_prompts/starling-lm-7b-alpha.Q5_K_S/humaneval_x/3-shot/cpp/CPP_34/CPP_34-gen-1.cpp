    vector<int> result;
    int i;
    for (i=0;i<l.size();i++)
    if (find(result.begin(), result.end(), l[i])==result.end())
    {
    result.push_back(l[i]);
    }
    sort(result.begin(), result.end());
    return result;
}


