    float mean = 0.0;
    float sum_deviation = 0.0;
    int i;
    float deviation;
    for (i=0;i<numbers.size();i++)
    {
        mean += numbers[i];
    }
    mean /= numbers.size();
    for (i=0;i<numbers.size();i++)
    {
        deviation = abs(numbers[i]-mean);
        sum_deviation += deviation;
    }
    return sum_deviation / numbers.size();
}