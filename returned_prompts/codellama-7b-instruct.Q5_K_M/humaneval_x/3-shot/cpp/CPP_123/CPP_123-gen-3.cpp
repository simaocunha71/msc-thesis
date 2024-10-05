    vector<int> odd_collatz;
    int i;
    for (i=1;i<=n;i++)
    {
        if (i%2!=0)
        odd_collatz.push_back(i);
    }
    return odd_collatz;
}



