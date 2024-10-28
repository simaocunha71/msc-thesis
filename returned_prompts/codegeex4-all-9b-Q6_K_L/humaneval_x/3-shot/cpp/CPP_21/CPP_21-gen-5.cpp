    float min_num=0;
    float max_num=0;
    int i;
    for (i=0;i<numbers.size();i++)
    if (numbers[i]<min_num)
    min_num=numbers[i];
    for (i=0;i<numbers.size();i++)
    if (numbers[i]>max_num)
    max_num=numbers[i];
    for (i=0;i<numbers.size();i++)
    {
    numbers[i]=(numbers[i]-min_num)/(max_num-min_num);
    }
    return numbers;
}

