    float sum=0;
    for (int i=0;i<numbers.size();i++)
    sum+=numbers[i];
    float mean=sum/numbers.size();
    float sum_deviation=0;
    for (int i=0;i<numbers.size();i++)
    sum_deviation+=abs(numbers[i]-mean);
    return sum_deviation/numbers.size();
}