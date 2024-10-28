    vector<int> odds;
    while (n != 1)
    {
        if (n % 2 != 0)
        {
            odds.push_back(n);
        }
        n = n % 2 ? n*3 + 1 : n / 2;
    }
    odds.push_back(1);
    sort(odds.begin(), odds.end());
    return odds;
}


