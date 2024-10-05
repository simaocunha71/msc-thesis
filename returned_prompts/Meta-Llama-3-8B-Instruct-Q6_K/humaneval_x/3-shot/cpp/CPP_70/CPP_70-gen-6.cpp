    vector<int> sorted;
    vector<int> lst_copy(lst);
    sort(lst_copy.begin(), lst_copy.end());
    while (!lst_copy.empty())
    {
        sorted.push_back(lst_copy.back());
        lst_copy.pop_back();
        if (!lst_copy.empty())
        {
            sort(lst_copy.begin(), lst_copy.end());
        }
    }
    return sorted;
}
```

