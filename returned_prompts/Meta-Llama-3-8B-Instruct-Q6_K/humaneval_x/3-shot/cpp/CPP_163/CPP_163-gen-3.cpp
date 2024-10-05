    vector<int> result;
    int min_val = min(a,b);
    int max_val = max(a,b);
    for (int i = min_val; i <= max_val; i++)
    {
        if (i % 2 == 0)
        {
            result.push_back(i);
        }
    }
    return result;
}