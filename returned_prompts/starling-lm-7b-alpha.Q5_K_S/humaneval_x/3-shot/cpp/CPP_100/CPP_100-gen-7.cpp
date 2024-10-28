    vector<int> pile;
    int curr=n;
    int i;
    for (i=0;i<n;i++)
    {
        pile.push_back(curr);
        curr+=i%2==0?1:2;
    }
    return pile;
}



