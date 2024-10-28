    float sum=0.0;
    float mean=0.0;
    float median=0.0;
    int i;
    mean=mean_of(numbers);
    for (i=0;i<numbers.size();i++)
    sum+=abs(numbers[i]-mean);
    median=sum/numbers.size();
    return median;
}

