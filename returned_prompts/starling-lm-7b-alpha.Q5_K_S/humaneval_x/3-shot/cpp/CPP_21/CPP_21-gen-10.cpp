    int i;
    float min,max,delta;
    min=numbers[0];
    max=numbers[0];
    for (i=1;i<numbers.size();i++)
    {
        if (numbers[i]<min)
        min=numbers[i];
        if (numbers[i]>max)
        max=numbers[i];
    }
    delta=max-min;
    for (i=0;i<numbers.size();i++)
    {
        numbers[i]=(numbers[i]-min)/delta;
    }
    return numbers;
}






