    int max;
    vector<int> roll;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        if (i==0)
        {
            max=numbers[i];
            roll.push_back(max);
        }
        if (i!=0)
        {
            if (numbers[i]>max)
            {
                max=numbers[i];
                roll.push_back(max);
            }
            if (numbers[i]<=max)
            {
                roll.push_back(max);
            }
        }
    }
    return roll;
}

