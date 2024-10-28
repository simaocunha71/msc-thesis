    int i;
    float min_v=numbers[0];
    float max_v=numbers[0];
    for (i=0;i<numbers.size();i++)
    {
        if (numbers[i]<min_v)
        min_v=numbers[i];
        if (numbers[i]>max_v)
        max_v=numbers[i];
    }
    for (i=0;i<numbers.size();i++)
    {
        numbers[i]=(numbers[i]-min_v)/(max_v-min_v);
    }
    return numbers;
}


