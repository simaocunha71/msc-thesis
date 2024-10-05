    float min=numbers[0], max=numbers[0];
    int i;
    for(i=0;i<numbers.size();i++)
    {
        if(numbers[i]<min)
        min=numbers[i];
        if(numbers[i]>max)
        max=numbers[i];
    }
    for(i=0;i<numbers.size();i++)
    numbers[i]=(numbers[i]-min)/(max-min);
    return numbers;
}

