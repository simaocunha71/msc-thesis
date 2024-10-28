    float sum=0.0;
    int i;
    for(i=0;i<numbers.size();i++)
    sum+=numbers[i];
    float mean=sum/numbers.size();
    float deviations_sum=0.0;
    for(i=0;i<numbers.size();i++)
    deviations_sum+=abs(numbers[i]-mean);
    return deviations_sum/numbers.size();
}


