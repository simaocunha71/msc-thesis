    vector<int> odds;
    while(n!=1)
    {
        if(n%2!=0)
        {
            odds.push_back(n);
        }
        if(n%2==0)
        {
            n=n/2;
        }
        else
        {
            n=3*n+1;
        }
    }
    sort(odds.begin(), odds.end());
    return odds;
}




