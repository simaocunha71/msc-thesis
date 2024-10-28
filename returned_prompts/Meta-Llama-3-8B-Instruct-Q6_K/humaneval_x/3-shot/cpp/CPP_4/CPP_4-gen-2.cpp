    float mean = 0.0;
    float sum = 0.0;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        mean += numbers[i];
    }
    mean /= numbers.size();
    for (i=0;i<numbers.size();i++)
    {
        sum += abs(numbers[i]-mean);
    }
    return sum / numbers.size();
}