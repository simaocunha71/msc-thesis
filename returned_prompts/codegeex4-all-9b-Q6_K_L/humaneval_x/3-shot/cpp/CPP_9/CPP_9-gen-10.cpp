    vector<int> all_rolling;
    int max_num=0;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        if (numbers[i]>max_num)
        {
            max_num=numbers[i];
        }
        all_rolling.push_back(max_num);
    }
    return all_rolling;
}

