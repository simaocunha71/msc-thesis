    float mean=0;
    float sum=0;
    int i;
    for (i=0;i<numbers.size();i++)
    sum+=numbers[i];
    mean=sum/numbers.size();
    float avg=0;
    for (i=0;i<numbers.size();i++)
    avg+=abs(numbers[i]-mean);
    avg=avg/numbers.size();
    return avg;
}


