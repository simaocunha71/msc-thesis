    float sum=0;
    float mean;
    int i;
    for(i=0;i<numbers.size();i++)
    sum+=numbers[i];
    mean=sum/numbers.size();
    sum=0;
    for(i=0;i<numbers.size();i++)
    sum+=abs(numbers[i]-mean);
    return sum/numbers.size();
}


