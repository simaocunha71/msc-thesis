    float min_val=min_element(numbers.begin(), numbers.end());
    float max_val=max_element(numbers.begin(), numbers.end());
    vector<float> rescaled;
    for (int i=0;i<numbers.size();i++)
    {
        rescaled.push_back((numbers[i]-min_val)/(max_val-min_val));
    }
    return rescaled;
}  