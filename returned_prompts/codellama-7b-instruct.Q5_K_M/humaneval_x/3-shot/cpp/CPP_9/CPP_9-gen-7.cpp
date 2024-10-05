    vector<int> maxes;
    maxes.push_back(numbers[0]);
    for (int i=1;i<numbers.size();i++)
    if (numbers[i]>maxes[i-1])
    maxes.push_back(numbers[i]);
    return maxes;
}


