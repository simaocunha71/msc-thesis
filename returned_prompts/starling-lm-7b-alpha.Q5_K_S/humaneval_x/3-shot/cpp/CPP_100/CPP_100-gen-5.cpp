    vector<int> all_pile;
    int i;
    int current_level=n;
    for (i=1;i<=n;i++)
    {
        if (i%2==0)
        {
            all_pile.push_back(current_level);
            current_level+=2;
        }
        if (i%2!=0)
        {
            all_pile.push_back(current_level);
            current_level+=1;
        }
    }
    return all_pile;
}




