    vector<int> maxes;
    int m = numbers[0];
    maxes.push_back(m);
    for(int i=1;i<numbers.size();i++)
    {
        if(numbers[i]>m)
        {
            m=numbers[i];
        }
        maxes.push_back(m);
    }
    return maxes;
}


