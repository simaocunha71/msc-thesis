    vector<int> integers;
    int current=a;
    while (current<=b)
    {
        if (current%2==0)
        integers.push_back(current);
        current+=1;
    }
    return integers;
}


