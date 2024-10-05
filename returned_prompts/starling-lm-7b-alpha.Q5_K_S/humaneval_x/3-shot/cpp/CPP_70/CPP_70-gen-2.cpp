    vector<int> result;
    int i;
    for (i=0;i<lst.size();i++)
    {
        result.push_back(lst[i]);
        sort(result.begin(),result.end());
        result.erase(min_element(result.begin(),result.end()));
    }
    return result;
}



