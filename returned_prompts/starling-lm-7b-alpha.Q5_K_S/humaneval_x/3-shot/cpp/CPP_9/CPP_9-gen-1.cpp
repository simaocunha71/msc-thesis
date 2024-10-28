    vector<int> maxes;
    int max_elem;
    int i,j;
    max_elem=numbers[0];
    maxes.push_back(numbers[0]);
    for (i=1;i<numbers.size();i++)
    {
        if (numbers[i]>max_elem)
        {
            max_elem=numbers[i];
        }
        maxes.push_back(max_elem);
    }

    return maxes;
}



