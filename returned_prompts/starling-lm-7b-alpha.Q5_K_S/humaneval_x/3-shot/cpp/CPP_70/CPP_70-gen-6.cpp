    int i;
    sort(lst.begin(), lst.end());
    vector<int> result;
    for (i=0;i<lst.size();i++)
    {
        if (i%2==0)
        result.insert(result.begin(), lst[i]);
        else
        result.push_back(lst[i]);
    }
    return result;
}


