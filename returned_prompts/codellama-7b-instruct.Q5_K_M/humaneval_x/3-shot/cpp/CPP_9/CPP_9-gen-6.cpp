    int max=numbers[0];
    int i;
    vector<int> max_sequence;
    for (i=0;i<numbers.size();i++)
    {
        if (numbers[i]>max)
        max=numbers[i];
        max_sequence.push_back(max);
    }
    return max_sequence;
}



