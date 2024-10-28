    vector<int> result;
    vector<int> sorted_lst(lst);
    sort(sorted_lst.begin(), sorted_lst.end());
    int i=0;
    while (!sorted_lst.empty())
    {
        result.push_back(sorted_lst.back());
        sorted_lst.pop_back();
        if (!sorted_lst.empty())
        {
            sorted_lst.erase(sorted_lst.begin());
        }
    }
    return result;
}