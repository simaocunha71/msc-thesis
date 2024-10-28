    float min_num=numbers[0];
    float max_num=numbers[0];
    float range=0;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        if (numbers[i]<min_num)
        min_num=numbers[i];
        if (numbers[i]>max_num)
        max_num=numbers[i];
    }
    range=max_num-min_num;
    vector<float> scaled_numbers(numbers.size());
    for (i=0;i<numbers.size();i++)
    scaled_numbers[i]=((numbers[i]-min_num)/range);
    return scaled_numbers;
}


