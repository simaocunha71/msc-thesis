    vector<int> all_stones;
    int i;
    int level=n;
    for (i=0;i<n;i++)
    {
        all_stones.push_back(level);
        if (level%2==0)
        level+=2;
        else
        level+=1;
    }
    return all_stones;
}


