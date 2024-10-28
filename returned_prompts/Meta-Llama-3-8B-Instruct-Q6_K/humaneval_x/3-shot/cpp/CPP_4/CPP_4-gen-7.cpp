    float mean = 0;
    float mad = 0;
    int i;
    float sum = 0;
    for (i=0;i<numbers.size();i++)
    {
        sum += numbers[i];
    }
    mean = sum / numbers.size();
    for (i=0;i<numbers.size();i++)
    {
        mad += abs(numbers[i]-mean);
    }
    return mad / numbers.size();
} 

