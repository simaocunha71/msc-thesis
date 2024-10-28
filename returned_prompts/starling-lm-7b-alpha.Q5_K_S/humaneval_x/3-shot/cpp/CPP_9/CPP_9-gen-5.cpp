    vector<int> maxes;
    int current_max;
    int i,j;
    for (i=0;i<numbers.size();i++)
    {
        current_max=numbers[i];
        for (j=i+1;j<numbers.size();j++)
        {
            if (numbers[j]>current_max)
            current_max=numbers[j];
        }
        maxes.push_back(current_max);
    }
    return maxes;
}



