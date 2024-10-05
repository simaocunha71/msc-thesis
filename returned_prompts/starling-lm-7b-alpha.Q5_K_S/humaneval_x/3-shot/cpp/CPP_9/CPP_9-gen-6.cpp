    vector<int> all_max;
    int current_max=-1;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        if (numbers[i]>current_max)
        {
            current_max=numbers[i];
            all_max.push_back(current_max);
        }
        else
        {
            all_max.push_back(current_max);
        }
    }
    return all_max;
}




