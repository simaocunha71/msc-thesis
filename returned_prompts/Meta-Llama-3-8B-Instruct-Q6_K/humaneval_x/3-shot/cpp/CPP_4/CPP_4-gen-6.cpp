    float mean;
    float sum = 0;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        sum += abs(numbers[i] - (mean = (sum / (i+1))));
    }
    return sum / numbers.size();
}
