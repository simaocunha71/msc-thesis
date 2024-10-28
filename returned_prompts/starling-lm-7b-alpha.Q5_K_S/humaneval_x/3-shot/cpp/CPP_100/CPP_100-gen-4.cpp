    vector<int> all_stones;
    int current_level=n;
    int i=0;
    while (current_level!=0)
    {
        all_stones.push_back(current_level);
        if (i%2==0 && current_level%2!=0)
        {
        current_level+=1;
        }
        if (i%2!=0 && current_level%2==0)
        {
        current_level+=1;
        }
        if (i%2!=0 && current_level%2!=0)
        {
        current_level-=1;
        }
        if (i%2==0 && current_level%2==0)
        {
        current_level-=1;
        }
        i+=1;
    }
    return all_stones;
}


