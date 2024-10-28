    float min_diff=INFINITY;
    float diff;
    vector<float> closest_pair;
    sort(numbers.begin(), numbers.end());
    for  (int i=0; i<numbers.size()-1; i++)
    {
        diff = numbers[i+1]-numbers[i];
        if  (diff<min_diff)
        {
            min_diff = diff;
            closest_pair = {numbers[i], numbers[i+1]};
        }
    }
    return closest_pair;
}

