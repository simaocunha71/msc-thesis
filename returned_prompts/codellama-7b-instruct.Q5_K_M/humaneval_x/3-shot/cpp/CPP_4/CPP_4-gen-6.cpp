    int i;
    float sum_deviations=0;
    float mean=0;
    float deviation;
    for (i=0;i<numbers.size();i++)
    {
        mean+=numbers[i];
    }
    mean/=numbers.size();
    for (i=0;i<numbers.size();i++)
    {
        deviation=numbers[i]-mean;
        sum_deviations+=fabs(deviation);
    }
    sum_deviations/=numbers.size();
    return sum_deviations;
}


