    float mean=0.0;
    float sum=0.0;
    float deviation=0.0;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
    }
    mean=sum/numbers.size();
    for (i=0;i<numbers.size();i++)
    {
        deviation+=abs(numbers[i]-mean);
    }
    deviation/=numbers.size();
    return deviation;
}



