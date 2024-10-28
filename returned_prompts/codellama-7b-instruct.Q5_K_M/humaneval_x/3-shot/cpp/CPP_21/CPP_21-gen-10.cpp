    float min=numbers[0], max=numbers[0];
    for (int i=0;i<numbers.size();i++)
    {
        if (numbers[i]<min)
        min=numbers[i];
        if (numbers[i]>max)
        max=numbers[i];
    }
    vector<float> rescaled_numbers;
    for (int i=0;i<numbers.size();i++)
    {
        rescaled_numbers.push_back((numbers[i]-min)/(max-min));
    }
    return rescaled_numbers;
}






