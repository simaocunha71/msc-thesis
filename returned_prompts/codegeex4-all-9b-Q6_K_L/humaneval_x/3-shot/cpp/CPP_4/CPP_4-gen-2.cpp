    float sum=0;
    int i;
    for (i=0;i<numbers.size();i++)
    sum+=numbers[i];
    float x_mean=sum/numbers.size();
    float total=0;
    for (i=0;i<numbers.size();i++)
    total+=abs(numbers[i]-x_mean);
    return total/numbers.size();
}

