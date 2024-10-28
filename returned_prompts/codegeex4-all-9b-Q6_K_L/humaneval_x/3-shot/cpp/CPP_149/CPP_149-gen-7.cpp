    vector<string> sorted;
    int i;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i].length()%2==0)
        sorted.push_back(lst[i]);
    }
    sort(sorted.begin(),sorted.end());
    return sorted;
}