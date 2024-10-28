    vector<int> trib;
    trib.push_back(1);
    trib.push_back(3);
    trib.push_back(2);
    int i;
    for (i=3;i<=n;i++)
    {
        if (i%2==0)
            trib.push_back(1+i/2);
        else
            trib.push_back(trib[i-1]+trib[i-2]+trib[i+1]);
    }
    return trib;
}