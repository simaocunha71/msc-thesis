    vector<pair<int, int>> p;
    int i;
    for (i=0;i<nums.size();i++)
    p.push_back({nums[i], i});

    sort(p.begin(), p.end(), [](pair<int, int>& a, pair<int, int>& b){
        if (a.first==b.first)
        return a.second<b.second;
        else
        return a.first<b.first;
    });

    vector<int> r;
    for (i=0;i<p.size();i++)
    r.push_back(p[i].first);

    return r;
}



