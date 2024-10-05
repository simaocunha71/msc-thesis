    vector<int> Trib;
    int i,j;
    Trib.push_back(1);
    Trib.push_back(3);
    for (i=2;i<=n;i++)
    {
        if (i%2==0)
        {
            Trib.push_back(1+i/2);
        }
        else
        {
            Trib.push_back(Trib[i-1]+Trib[i-2]+Trib[i-3]);
        }
    }
    return Trib;
}

