    float min_number=numbers[0];
    float max_number=numbers[0];
    int i;
    for (i=1;i<numbers.size();i++)
    {
        if (numbers[i]<min_number)
        min_number=numbers[i];
        if (numbers[i]>max_number)
        max_number=numbers[i];
    }
    float range=max_number-min_number;
    vector<float> scaled_numbers;
    for (i=0;i<numbers.size();i++)
    {
        float scaled=numbers[i]-min_number;
        scaled=scaled/range;
        scaled_numbers.push_back(scaled);
    }
    return scaled_numbers;
}


