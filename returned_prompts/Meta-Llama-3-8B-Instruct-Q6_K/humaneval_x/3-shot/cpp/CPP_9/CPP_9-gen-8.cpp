    vector<int> result;
    int max_so_far = numbers[0];
    result.push_back(max_so_far);
    for (int i=1; i<numbers.size(); i++)
    {
        if (numbers[i] > max_so_far)
        {
            max_so_far = numbers[i];
        }
        result.push_back(max_so_far);
    }
    return result;
}