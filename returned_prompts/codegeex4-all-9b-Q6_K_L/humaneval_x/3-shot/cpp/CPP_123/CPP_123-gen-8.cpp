    vector<int> odd_collatz;
    int i=n;
    while(i>1)
    {
        if (i%2==1)
            odd_collatz.push_back(i);
        if (i%2==0)
            i=i/2;
        else
            i=3*i+1;
    }
    sort(odd_collatz.begin(),odd_collatz.end());
    return odd_collatz;
}