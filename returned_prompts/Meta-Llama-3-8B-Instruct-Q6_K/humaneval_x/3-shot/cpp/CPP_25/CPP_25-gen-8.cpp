    vector<int> factors;
    for (int i=2;i<=n;i++)
    {
        while (n%i==0)
        {
            factors.push_back(i);
            n=n/i;
        }
    }
    return factors;
}  // This function will not work correctly for big numbers, because it's not optimized.  // This function will not work correctly for big numbers, because it's not optimized.