    float min_diff = INFINITY;
    vector<float> closest_pair;
    sort(numbers.begin(), numbers.end());
    for (int i = 0; i < numbers.size()-1; ++i)
    {
        if (numbers[i+1]-numbers[i] < min_diff)
        {
            min_diff = numbers[i+1]-numbers[i];
            closest_pair = {numbers[i], numbers[i+1]};
        }
    }
    return closest_pair;
}

