    vector<int> result;
    int stones=n;
    for (int i=0;i<n;i++)
    {
        result.push_back(stones);
        if (stones%2==0)
        {
            stones+=2;
        }
        else
        {
            stones+=2;
        }
    }
    return result;
}

