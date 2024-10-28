    vector<int> all_factors;
    for (int i=2;i<=n;i++)
    if (n%i==0)
    {
        all_factors.push_back(i);
        while (n%i==0)
        n/=i;
    }

    return all_factors;
}



