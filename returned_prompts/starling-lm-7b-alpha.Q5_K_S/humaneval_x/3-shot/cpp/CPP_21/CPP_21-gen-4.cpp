    int i;
    float max_val=numbers[0];
    float min_val=numbers[0];
    int size=numbers.size();
    for (i=0;i<size;i++)
    {
        if (numbers[i]>max_val)
        max_val=numbers[i];
        if (numbers[i]<min_val)
        min_val=numbers[i];
    }
    vector<float> new_numbers;
    for (i=0;i<size;i++)
    {
        new_numbers.push_back((numbers[i]-min_val)/(max_val-min_val));
    }
    return new_numbers;
}


