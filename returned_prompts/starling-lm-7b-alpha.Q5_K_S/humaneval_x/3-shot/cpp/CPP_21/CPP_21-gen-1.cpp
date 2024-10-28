    float min_num=numbers[0];
    float max_num=numbers[0];
    int i;
    for (i=0;i<numbers.size();i++)
    {
        min_num=min(min_num,numbers[i]);
        max_num=max(max_num,numbers[i]);
    }
    for (i=0;i<numbers.size();i++)
    {
        numbers[i]=(numbers[i]-min_num)/(max_num-min_num);
    }
    return numbers;
}



