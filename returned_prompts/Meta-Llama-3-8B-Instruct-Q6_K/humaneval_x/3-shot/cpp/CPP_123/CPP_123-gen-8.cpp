    vector<int> collatz;
    int i;
    for (i=n; i>1; i=i%2==0 ? i/2 : 3*i+1)
    if (i%2!=0)
    collatz.push_back(i);
    sort(collatz.begin(), collatz.end());
    return collatz;
}